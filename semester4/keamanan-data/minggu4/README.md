# Tugas Kriptografi: Implementasi RSA (Asymmetric Cryptography)

Directory ini berisi implementasi algoritma kriptografi asimetris **RSA
(Rivest, Shamir, and Adleman)** menggunakan bahasa pemrograman Python. Kode ini
dibuat untuk memenuhi tugas mata kuliah Keamanan Data / Kriptografi, sesuai
dengan instruksi untuk mengimplementasikan algoritma dari kategori kriptografi
asimetris.

## Struktur Kode

Implementasi RSA di dalam file `RSA_tugas.py` mencakup:

- **`calculate_gcd`**: Mencari nilai FPB (Faktor Persekutuan Terbesar)
  menggunakan algoritma Euclidean.
- **`modular_exponentiation`**: Implementasi manual untuk menghitung
  eksponensiasi modular (_Square-and-Multiply_) guna memproses enkripsi dan
  dekripsi secara efisien tanpa menggunakan fungsi bawaan seperti `pow()`.
- **`calculate_mod_inverse`**: Menghitung _Modular Multiplicative Inverse_
  untuk mendapatkan eksponen kunci privat (`d`).
- **`generate_rsa_keys`**: Membangkitkan pasangan kunci asimetris: **Kunci
  Publik** (untuk mengenkripsi) dan **Kunci Privat** (untuk mendekripsi).
- **`rsa_encrypt` & `rsa_decrypt`**: Mengubah string (Plaintext) menjadi array
  of bytes (Ciphertext) dan sebaliknya.

## Persyaratan (Prerequisites)

Sebelum menjalankan program ini, pastikan sistem Anda telah memenuhi prasyarat
berikut:

- **Git**: Untuk mengclone repositori ke storage lokal kalian.
- **Python 3.x**: _Interpreter_ utama untuk menjalankan _script_. Tidak ada
  _library_ eksternal yang diwajibkan.

## Cara Menjalankan (Step-by-Step)

### 1. Clone Repositori

Buka Terminal (Linux/macOS) atau Command Prompt/PowerShell (Windows), lalu
jalankan perintah berikut untuk mengunduh _source code_:

```bash
git clone https://github.com/DinkyTrady/colleges.git
cd colleges/semester4/keamanan-data/minggu4/
```

### 2. Menjalankan Kode Program

Anda bisa memilih salah satu dari dua metode di bawah ini untuk mengeksekusi
_file_:

Ketik dan jalankan perintah berikut:

```bash
python RSA_tugas.py
```

_(Catatan: Jika menggunakan Linux/macOS, gunakan perintah `python3
RSA_tugas.py`)_

## Contoh Hasil Eksekusi (Output)

Saat _script_ berhasil berjalan, program akan menggenerasi kunci, melakukan
proses enkripsi dan dekripsi dari kata "Ini adalah RSA Algorithm dari awal (scratcth)", lalu
menampilkannya di layar:

```text
Kunci Publik  (e, n): (7, 3233)
Kunci Private (d, n): (1783, 3233)
Pesan asli: Ini adalah RSA Algorithm dari awal (scratcth)
Hasil Enkripsi (Array angka): [286, 1544, 3020, 2774, 1818, 2872, 1818, 1877, 1818, 3052, 2774, 1077, 1825, 1317, 2774, 1317, 1
877, 728, 3183, 1797, 3020, 1762, 3052, 597, 2774, 2872, 1818, 1797, 3020, 2774, 1818, 863, 1818, 1877, 2774, 1363, 567, 24, 17
97, 1818, 1762, 24, 1762, 3052, 2711]
Hasil dekripsi: Ini adalah RSA Algorithm dari awal (scratcth)
```
