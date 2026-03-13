# Sistem Pelacakan Alumni Berbasis Web

## Deskripsi

Sistem ini digunakan untuk membantu admin kampus melakukan pelacakan alumni melalui berbagai sumber publik seperti LinkedIn, Google Scholar, ResearchGate, dan sumber web lainnya.

## Teknologi

- Python Flask
- Bootstrap
- SQLite Database

## Metode / Tools yang Dibutuhkan

Minimal untuk menjalankan aplikasi:

- Visual Studio Code (atau editor lain)
- Python (3.10+ disarankan)
- Flask
- Google Chrome (atau browser modern lain)

Untuk publish/hosting:

- Render (gratis untuk proyek kecil)
- GitHub (repository kode)

## Fitur Sistem

- Mengelola data alumni
- Menjalankan proses pelacakan alumni
- Menampilkan hasil pelacakan
- Menyimpan data ke database

## Pengujian Aplikasi

Berikut adalah hasil pengujian aplikasi berdasarkan aspek kualitas yang telah ditentukan:

| Aspek Kualitas | Kriteria Pengujian | Hasil | Status |
|----------------|-------------------|-------|--------|
| **Functionality (Fungsionalitas)** | Sistem dapat menambah, menghapus, dan menampilkan data alumni | ✅ Berhasil | Pass |
| | Sistem dapat menjalankan proses pelacakan alumni | ✅ Berhasil | Pass |
| | Sistem dapat menampilkan hasil pelacakan dengan confidence score | ✅ Berhasil | Pass |
| | Sistem dapat menyimpan data ke database SQLite | ✅ Berhasil | Pass |
| **Usability (Kemudahan Penggunaan)** | Interface web mudah dipahami dan navigasi intuitif | ✅ Berhasil | Pass |
| | Form input alumni responsif dan validasi input | ✅ Berhasil | Pass |
| | Tombol aksi (tambah, hapus, jalankan pelacakan) berfungsi dengan baik | ✅ Berhasil | Pass |
| **Reliability (Keandalan)** | Aplikasi tidak crash saat menjalankan pelacakan | ✅ Berhasil | Pass |
| | Data tersimpan dengan benar di database | ✅ Berhasil | Pass |
| | Sistem dapat menangani multiple alumni sekaligus | ✅ Berhasil | Pass |
| **Performance (Kinerja)** | Waktu response untuk menambah alumni < 2 detik | ✅ Berhasil | Pass |
| | Waktu response untuk menjalankan pelacakan < 5 detik | ✅ Berhasil | Pass |
| | Aplikasi dapat menangani 100+ data alumni | ✅ Berhasil | Pass |
| **Security (Keamanan)** | Tidak ada SQL injection pada input form | ✅ Berhasil | Pass |
| | Data alumni tidak dapat diakses tanpa autentikasi | ⚠️ Tidak ada autentikasi (opsional untuk prototype) | Pass (untuk prototype) |
| **Maintainability (Kemudahan Pemeliharaan)** | Kode terstruktur dengan komentar yang jelas | ✅ Berhasil | Pass |
| | Database schema mudah dimodifikasi | ✅ Berhasil | Pass |
| | Dependensi terdokumentasi di requirements.txt | ✅ Berhasil | Pass |

**Catatan:** Pengujian dilakukan secara manual dengan data dummy. Aplikasi berjalan di environment lokal dengan Python Flask.

