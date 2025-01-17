import mysql.connector


"""
Jika kamu mengalami masalah pada saat menjalankan kode ini, 
ikuti langkah berikut:
    mysql -u root
    
Jalankan perintah berikut untuk memeriksa plugin autentikasi yang 
digunakan oleh user root:
    SELECT user, host, plugin FROM mysql.user WHERE user = 'root';

Jika plugin yang digunakan adalah auth_socket, maka jalankan perintah 
berikut untuk mengatur ulang password root:
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password'; 

Gantilah 'new_password' dengan password yang baru yang mudah diingat

Setelah mengatur ulang password, Anda dapat memeriksa plugin autentikasi 
yang digunakan oleh root dengan menjalankan perintah berikut:
    SELECT user, host, plugin FROM mysql.user WHERE user = 'root';

Pastikan plugin untuk root sekarang adalah mysql_native_password, 
Setelah berhasil mengatur ulang password, jalankan perintah untuk memperbarui hak akses:
    FLUSH PRIVILEGES;

Keluar dari sesi MySQL dengan perintah:
EXIT;

semoga terkoneksi dengan baik.
"""

# Membuat koneksi ke MySQL
db_connection = mysql.connector.connect(
    host="localhost",  # Ganti dengan host MySQL Anda jika diperlukan
    user="root",       # Ganti dengan username MySQL Anda
    password="1234",       # Ganti dengan password MySQL Anda
)

cursor = db_connection.cursor()

# Membuat database jika belum ada
cursor.execute("CREATE DATABASE IF NOT EXISTS inventory_db")

# Menggunakan database yang baru dibuat
cursor.execute("USE inventory_db")

# Membuat tabel barang jika belum ada
create_table_query = """
CREATE TABLE IF NOT EXISTS barang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_barang VARCHAR(255) NOT NULL,
    kategori VARCHAR(100) NOT NULL,
    stok INT DEFAULT 0,
    harga DECIMAL(10, 2) DEFAULT 0.00,
    deskripsi TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
cursor.execute(create_table_query)

# Menambahkan beberapa data contoh
insert_data_query = """
INSERT INTO barang (nama_barang, kategori, stok, harga, deskripsi) VALUES
('Laptop Dell XPS 13', 'Elektronik', 5, 15000000.00, 'Laptop premium dengan layar 13 inci'),
('Mouse Logitech MX Master 3', 'Aksesori', 10, 1200000.00, 'Mouse nirkabel dengan desain ergonomis'),
('Smartphone Samsung Galaxy S22', 'Elektronik', 8, 9500000.00, 'Smartphone flagship dengan kamera 108MP'),
('Meja Kerja Minimalis', 'Perabot', 20, 2000000.00, 'Meja kerja dengan desain minimalis dan elegan');
"""
cursor.execute(insert_data_query)

# Commit perubahan ke database
db_connection.commit()

# Menutup koneksi
cursor.close()
db_connection.close()

print("Database dan tabel berhasil dibuat, serta data contoh berhasil ditambahkan.")
