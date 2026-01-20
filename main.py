import cv2
import numpy as np

# =========================
# 1) Baca gambar dalam mode grayscale
# cv2.IMREAD_GRAYSCALE -> hasilnya 1 channel (0-255)
# =========================
img = cv2.imread("ti_unusia.jpg", cv2.IMREAD_GRAYSCALE)

# Kalau file tidak ada / gagal dibaca, cv2.imread akan mengembalikan None
if img is None:
    raise FileNotFoundError("ti_unusia.jpg tidak ditemukan")

# =========================
# 2) Ubah tipe data ke float32
# Ini penting karena cv2.dct membutuhkan input float (bukan uint8),
# dan hasil DCT berupa bilangan desimal.
# =========================
img = img.astype(np.float32)

# =========================
# 3) Parameter steganografi
# block_size = 8 artinya gambar dibagi per blok 8x8 (sesuai petunjuk)
# cy, cx adalah posisi koefisien DCT tempat bit disembunyikan
# contoh: (4,4) berarti baris ke-4 kolom ke-4 (indeks dimulai dari 0)
# =========================
block_size = 8
cy, cx = 4, 4
bits = []  # list untuk menampung bit hasil ekstraksi ('0' atau '1')

# Ambil tinggi (h) dan lebar (w) gambar
h, w = img.shape

# =========================
# 4) Iterasi gambar blok demi blok ukuran 8x8
# range(0, h - block_size + 1, block_size)
# artinya: mulai dari 0, sampai batas blok terakhir, loncat per 8 piksel
# =========================
for y in range(0, h - block_size + 1, block_size):
    for x in range(0, w - block_size + 1, block_size):

        # Ambil satu blok 8x8 dari gambar
        block = img[y:y+block_size, x:x+block_size]

        # =========================
        # Optional: Centering sebelum DCT
        # Dalam standar JPEG, biasanya blok dikurangi 128 agar nilai piksel
        # berpusat di sekitar nol (range kira-kira -128 s/d 127)
        # TAPI ini tergantung metode penyisipan yang digunakan.
        # Jika encoding-nya memakai centering, decoding juga harus sama.
        # =========================
        # block = block - 128

        # =========================
        # 5) Hitung DCT untuk blok 8x8
        # Output: matriks 8x8 berisi koefisien frekuensi
        # =========================
        dct_block = cv2.dct(block)

        # Ambil satu koefisien DCT pada posisi (cy, cx)
        coeff = dct_block[cy, cx]

        # =========================
        # 6) Ekstraksi bit berdasarkan tanda koefisien
        # Jika coeff > 0 -> bit = 1
        # Jika coeff <= 0 -> bit = 0
        # =========================
        bits.append('1' if coeff > 0 else '0')

# =========================
# 7) Rekonstruksi bit -> teks ASCII
# Setiap 8 bit digabung menjadi 1 byte, lalu diubah menjadi karakter.
# =========================
decoded_text = ""

for i in range(0, len(bits), 8):
    byte = bits[i:i+8]  # ambil 8 bit (1 byte)
    if len(byte) < 8:
        break  # kalau sisa bit kurang dari 8, berhenti

    # Ubah 8 bit biner menjadi integer, lalu ke karakter ASCII
    decoded_text += chr(int("".join(byte), 2))

# =========================
# 8) Output
# - Panjang teks hasil decode
# - Preview 200 karakter pertama
# encode("unicode_escape") membuat karakter non-printable (mis. NULL \x00)
# terlihat jelas sebagai "\x00" di output terminal.
# =========================
print(f"Panjang teks hasil decode: {len(decoded_text)}")
print("Preview karakter:")
print(decoded_text[:200].encode("unicode_escape").decode())
