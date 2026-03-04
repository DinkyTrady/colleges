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
Kunci Publik  (e, n): (17, 3233)
Kunci Private (d, n): (2753, 3233)
Pesan asli: Ini adalah RSA Algorithm dari awal (scratcth)
Hasil Enkripsi (Array angka): [1486, 2235, 3179, 1992, 1632, 1773, 1632, 745, 1632, 2170, 1992, 1859, 2680, 2790, 1992, 2790, 7
45, 2923, 2185, 2412, 3179, 884, 2170, 2271, 1992, 1773, 1632, 2412, 3179, 1992, 1632, 1107, 1632, 745, 1992, 642, 1230, 281, 2
412, 1632, 884, 281, 884, 2170, 3199]
Hasil dekripsi: Ini adalah RSA Algorithm dari awal (scratcth)
```
