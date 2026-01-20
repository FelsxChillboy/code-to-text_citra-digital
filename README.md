Metode yang Digunakan
Citra dibagi menjadi blok 8×8 piksel
Setiap blok ditransformasikan ke domain frekuensi menggunakan DCT
Satu koefisien DCT dipilih sebagai tempat penyimpanan bit
Logika bit:
Koefisien > 0 → bit 1
Koefisien ≤ 0 → bit 0
Bit-bit dikumpulkan dan dikelompokkan menjadi byte (8 bit)
Byte dikonversi menjadi karakter ASCII
Pesan asli diakhiri dengan delimiter ###

⚙️ Kebutuhan Sistem
Python 3.8 atau lebih baru
Library:
opencv-python
numpy
Instalasi Library
pip install opencv-python numpy

▶️ Cara Menjalankan Program
clone dulu 
Pastikan file gambar berada di folder yang sama dengan program, lalu jalankan:
python main.py

📤 Contoh Output
Panjang teks hasil decode: 1536
Preview karakter:
IA###@\x00\x00\x00\x00\x00\x00\x00\x00\x00...
Keterangan:
IA### → pesan rahasia
\x00 → noise hasil decoding setelah pesan utama
Preview ditampilkan untuk 200 karakter pertama

📝 Catatan Teknis
Program menampilkan hasil decode mentah (raw) tanpa memotong delimiter
Untuk menghentikan pembacaan saat menemukan ###, tambahkan pengecekan delimiter saat proses rekonstruksi
Jika hasil tidak terbaca:
Coba aktifkan centering (block = block - 128)
Coba posisi koefisien DCT lain seperti (3,4) atau (4,3)


👤 Penulis
[ahmad azarruddin]
Program Studi Teknik Informatika
Universitas Nahdlatul Ulama Indonesia (UNUSIA)
