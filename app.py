import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Konfigurasi koneksi database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
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

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM barang")
    items = cur.fetchall()
    print("Data from database:", items)  # Menampilkan data hasil query untuk debugging
    cur.close()
    conn.close()
    return render_template('index.html', items=items)

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
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    if query:
        cur.execute("SELECT * FROM barang WHERE nama_barang LIKE %s OR kategori LIKE %s", ('%' + query + '%', '%' + query + '%'))
    else:
        cur.execute("SELECT * FROM barang")
    items = cur.fetchall()
    print("Search results:", items)  # Menampilkan hasil pencarian untuk debugging
    cur.close()
    conn.close()
    return render_template('search_results.html', items=items)

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
