"""
Tugas Kriptografi
Implementasi Algoritma dari Kategori:
B. Kriptografi Asimetris (Asymmetric)
Algoritma Terpilih: RSA (Rivest, Shamir, and Adleman)
"""


# Fungsi untuk mencari Faktor Persekutuan Terbesar (FPB) atau Greatest Common Divisor (GCD)
# Digunakan dalam RSA untuk mencari kunci publik 'e' yang relatif prima terhadap (phi).
def calculate_gcd(a, b):
    # Menggunakan Algoritma Euclidean untuk mencari nilai Faktor Persekutuan Terbesar (FPB)
    # Terus iterasi dengan nilai sisa bagi hingga mencapai 0
    while b != 0:
        a, b = b, a % b

    return a


# Fungsi Eksponensiasi Modular berbasis algoritma Square-and-Multiply.
# Digunakan secara ekstensif dalam proses enkripsi maupun dekripsi pada Kriptografi Asimetris (RSA).
# Menghitung (base^exponent) mod modulus secara efisien.
def modular_exponentiation(base, exponent, modulus):
    # Basis kasus standar: angka apa pun mod 1 selalu nilainya 0
    if modulus == 1:
        return 0

    result = 1
    base %= modulus

    while exponent > 0:
        # Jika bit eksponen ganjil (bit terakhir adalah 1)
        # Kalikan dengan nilai yang sudah diakumulasi mod modulus
        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent = exponent >> 1
        base = (base * base) % modulus

    return result


# Fungsi untuk menghitung Modular Multiplicative Inverse.
# Berfungsi untuk membangkitkan kunci privat 'd' dari kunci publik 'e', di mana (d * e) mod phi = 1.
def calculate_mod_inverse(e, phi):
    # Mencari nilai eksponen privat d secara sekuensial (bruteforce)
    # Persamaan (d * e) % phi harus menghasilkan 1 (identitas kebalikan / modular multiplicative)
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None


# Fungsi perumusan Asymmetric Key Pair (Kunci Publik dan Kunci Privat).
# Melibatkan dua bilangan prima rahasia (p dan q) untuk membentuk modulus n dan nilai phi.
def generate_rsa_keys(p, q):
    # n berperan sebagai modulus penyamaan hitungan kunci publik dan privat
    n = p * q
    # phi adalah nilai Fungsi Totient Euler untuk mencari keunikan e dan d
    phi = (p - 1) * (q - 1)

    # e (eksponen publik) dimulai dari konstanta bilangan prima 17
    e = 17
    # Terus tambahkan jika e belum relatif prima / koprima terhadap ukuran phi (FPB bukan 1)
    while calculate_gcd(e, phi) != 1:
        e += 2

    # Menghitung ukuran variabel d (eksponen privat) melalui modular inverse dari kembaran e
    d = calculate_mod_inverse(e, phi)

    # Merakit tupel menjadi sistem sandi Asimetris sepasang: Public Key & Private Key
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


# Proses Enkripsi Asimetris RSA
# Teks pesan dienkripsi hanya menggunakan Kunci Publik pengirim, merubah nilai byte aslinya.
def rsa_encrypt(message, public_key):
    # Ekstraksi tupel sandi publik
    e, n = public_key
    # Ubah format string pesan standar menjadi deretan array bytes
    message_bytes = message.encode("utf-8")

    # Mengeksekusi proses Kriptografi Asimetrik
    # Tiap byte masuk pada perumusan RSA Enkripsi (C = M^e mod n)
    ciphertext = [modular_exponentiation(byte, e, n) for byte in message_bytes]

    return ciphertext


# Proses Dekripsi Asimetris RSA
# Ciphertext yang dienkripsi dengan kunci publik hanya dapat didekripsi / dibuka dengan Kunci Privat pasangan aslinya.
def rsa_decrypt(ciphertext, private_key):
    # Ekstraksi tupel rahasia (Sandi Privat)
    d, n = private_key
    # Dekripsi asimetrik memakai formula sebaliknya (M = C^d mod n) pada setiap angka ciphertext
    decrypted_bytes = bytes(
        [modular_exponentiation(char_num, d, n) for char_num in ciphertext]
    )
    # Kembalikan tipe bytes angka menjadi teks string (plain text)
    real_message = decrypted_bytes.decode("utf-8")
    return real_message


p = 61
q = 53

public_key, private_key = generate_rsa_keys(p, q)
print(f"Kunci Publik  (e, n): {public_key}")
print(f"Kunci Private (d, n): {private_key}")

message = "Ini adalah RSA Algorithm dari awal (scratcth)"
print(f"Pesan asli: {message}")

secret_message = rsa_encrypt(message, public_key)
print(f"Hasil Enkripsi (Array angka): {secret_message}")

decrypt_message = rsa_decrypt(secret_message, private_key)
print(f"Hasil dekripsi: {decrypt_message}")
