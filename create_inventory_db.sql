-- Membuat database inventory_db
CREATE DATABASE IF NOT EXISTS inventory_db;

-- Menggunakan database inventory_db
USE inventory_db;

-- Membuat tabel barang untuk menyimpan data inventaris
CREATE TABLE IF NOT EXISTS barang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_barang VARCHAR(255) NOT NULL,
    kategori VARCHAR(100) NOT NULL,
    stok INT DEFAULT 0,
    harga DECIMAL(10, 2) DEFAULT 0.00,
    deskripsi TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Menambahkan beberapa data contoh (opsional)
INSERT INTO barang (nama_barang, kategori, stok, harga, deskripsi) VALUES
('Laptop Dell XPS 13', 'Elektronik', 5, 15000000.00, 'Laptop premium dengan layar 13 inci'),
('Mouse Logitech MX Master 3', 'Aksesori', 10, 1200000.00, 'Mouse nirkabel dengan desain ergonomis'),
('Smartphone Samsung Galaxy S22', 'Elektronik', 8, 9500000.00, 'Smartphone flagship dengan kamera 108MP'),
('Meja Kerja Minimalis', 'Perabot', 20, 2000000.00, 'Meja kerja dengan desain minimalis dan elegan');
