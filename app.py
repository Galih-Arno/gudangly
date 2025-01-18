import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_paginate import Pagination

app = Flask(__name__)

# Konfigurasi koneksi database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'inventory_db'

# Koneksi ke database MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    print("Database connected successfully!")  # Menambahkan log untuk memastikan koneksi berhasil
    return connection

def get_page_args(page_parameter='page', per_page_parameter='per_page'):
    page = request.args.get(page_parameter, 1, type=int)
    per_page = request.args.get(per_page_parameter, 5, type=int)
    return page, per_page

def get_paginated_items(query, page, per_page):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    # Query untuk menghitung total jumlah barang
    count_query = "SELECT COUNT(*) FROM (" + query + ") AS total"
    cur.execute(count_query)
    total_items = cur.fetchone()['COUNT(*)']
    
    # Hitung offset dan buat query dengan parameterized query
    offset = (page - 1) * per_page
    paginated_query = f"{query} LIMIT %s OFFSET %s"
    
    # Eksekusi query dengan parameter untuk limit dan offset
    cur.execute(paginated_query, (per_page, offset))
    items = cur.fetchall()
    cur.close()
    conn.close()
    return items, total_items

@app.route('/')
def index():
    page, per_page = get_page_args(page_parameter='page', per_page_parameter='per_page')
    per_page = 5    
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    query = "SELECT * FROM barang"
    items, total_items = get_paginated_items(query, page, per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total_items, record_name='items')
    # items = cur.fetchall()
    cur.close()
    conn.close()
    current_year = datetime.now().year
    return render_template('index.html', items=items, current_year=current_year, pagination=pagination)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        kategori = request.form['kategori']
        stok = request.form['stok']
        harga = request.form['harga']
        deskripsi = request.form['deskripsi']
        
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("INSERT INTO barang (nama_barang, kategori, stok, harga, deskripsi) VALUES (%s, %s, %s, %s, %s)",
                    (nama_barang, kategori, stok, harga, deskripsi))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM barang WHERE id = %s", (item_id,))
    item = cur.fetchone()
    if item is None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        kategori = request.form['kategori']
        stok = request.form['stok']
        harga = request.form['harga']
        deskripsi = request.form['deskripsi']
        
        cur.execute("UPDATE barang SET nama_barang = %s, kategori = %s, stok = %s, harga = %s, deskripsi = %s WHERE id = %s",
                    (nama_barang, kategori, stok, harga, deskripsi, item_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    cur.close()
    conn.close()
    return render_template('edit_item.html', item=item)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    page, per_page = get_page_args(page_parameter='page', per_page_parameter='per_page')
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    if query:
        query = f"SELECT * FROM barang WHERE nama_barang LIKE '%{query}%' OR kategori LIKE '%{query}%'"
    else:
        query = "SELECT * FROM barang"
    items, total_items = get_paginated_items(query, page, per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total_items, record_name='items')
    # items = cur.fetchall()
    cur.close()
    conn.close()
    current_year = datetime.now().year
    return render_template('search_results.html', items=items, current_year=current_year, pagination=pagination)

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM barang WHERE id = %s", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
