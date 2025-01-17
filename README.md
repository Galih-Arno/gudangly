# Aplikasi Manajemen Inventaris

Aplikasi Manajemen Inventaris adalah aplikasi berbasis web yang dibangun menggunakan **Flask**, **MySQL**, dan **Bootstrap** untuk mengelola stok barang, menambah, mengedit, dan menghapus barang dari inventaris. Aplikasi ini juga dilengkapi dengan antarmuka pengguna yang responsif dan halaman loading saat pertama kali membuka aplikasi.

## Fitur
- **Manajemen Barang**: Menambah, mengedit, dan menghapus data barang.
- **Kategori Barang**: Mengelompokkan barang berdasarkan kategori.
- **Monitoring Stok**: Melihat stok barang yang tersedia.
- **Halaman Loading**: Menampilkan halaman loading sementara aplikasi dimuat.
- **Responsive Design**: Antarmuka pengguna responsif menggunakan **Bootstrap**.

## Teknologi
- **Python**: Bahasa pemrograman untuk backend aplikasi.
- **Flask**: Framework Python untuk aplikasi web.
- **MySQL**: Database yang digunakan untuk menyimpan data barang.
- **HTML** & **Bootstrap**: Untuk membangun antarmuka pengguna responsif.
- **JavaScript**: Digunakan untuk menampilkan halaman loading.

## Persyaratan
Sebelum memulai proyek ini, pastikan Anda memiliki perangkat lunak berikut:
- **Python** (versi 3.x)
- **MySQL** (atau MariaDB)
- **XAMPP** (untuk menjalankan MySQL server)
- **Flask** dan **MySQL Connector** (atau Flask-MySQLdb)

### Instalasi
Ikuti langkah-langkah berikut untuk mengatur proyek ini di mesin lokal Anda:

1. **Clone repositori**:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. **Install dependensi**:
    Pastikan Anda sudah menginstal `pip` untuk mengelola dependensi Python. Jalankan perintah berikut untuk menginstal Flask dan MySQL Connector:
    ```bash

    pip install flask mysql-connector-python
    ```

3. **Setup Database**:
Sesuaikan pengaturan koneksi database di file `createDB.py` dengan kredensial MySQL Anda:
    ```bash
    python createDB.py
    ```

4. **Konfigurasi koneksi database**:
    Sesuaikan pengaturan koneksi database di file `app.py` dengan kredensial MySQL Anda:
    ```python
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'  # Ganti dengan username MySQL Anda
    app.config['MYSQL_PASSWORD'] = ''  # Ganti dengan password MySQL Anda
    app.config['MYSQL_DB'] = 'inventaris_db'
    ```

5. **Jalankan aplikasi**:
    Setelah semuanya terkonfigurasi, jalankan aplikasi Flask menggunakan perintah berikut:
    ```bash
    python app.py
    ```

    Aplikasi akan berjalan di `http://127.0.0.1:5000/` (atau port lain yang telah Anda tentukan).

## Struktur Proyek
Berikut adalah struktur direktori proyek ini:
proyek_inventory/ 
├── app.py # File utama aplikasi Flask 
├── templates/ 
    ├── index.html # Halaman utama aplikasi
    ├── add_item.html # Halaman untuk menambah barang
    └── edit_item.html # Halaman untuk mengedit barang 
└── static/ 
    └── css/ 
            ── style.css # Kustomisasi CSS tambahan

# Tugas: Aplikasi Manajemen Inventaris
- Tambahkan fitur untuk **info**, **tambah**, **hapus**, dan **edit**.
- Ubah Navbar **cari barang** menjadi **search button**.
- Buat **Pagination** jika daftar barangnya ada banyak.


## Lisensi
Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
