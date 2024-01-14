from google.colab import files
from PIL import Image
import cv2
import numpy as np
import io
import matplotlib.pyplot as plt
from IPython.display import display, Javascript

# Fungsi untuk mendapatkan path dari file yang diupload
def get_uploaded_file_path():
    display(Javascript('google.colab.output.setIframeHeight(0, true, {maxHeight: 300})'))
    uploaded = files.upload()
    file_path = list(uploaded.keys())[0]
    return file_path

# Meminta pengguna untuk memilih file gambar
nama_file_gambar = get_uploaded_file_path()

# Baca gambar dari path yang dipilih
gambar = Image.open(nama_file_gambar)

# Konversi gambar PIL menjadi array NumPy
gambar_array = np.array(gambar)

# Menampilkan informasi dan nilai piksel dari gambar
print(f"Informasi Gambar {nama_file_gambar}:")
print(f"Ukuran Gambar: {gambar.size}")
print(f"Mode Gambar: {gambar.mode}")
print(f"Nilai Piksel Gambar (beberapa contoh):")
print(gambar_array[:5, :5, :])  # Menampilkan beberapa piksel pertama sebagai contoh

# Membuat subplot dengan 1 baris dan 2 kolom untuk menampilkan gambar secara horizontal
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Menampilkan gambar asli di subplot pertama
axs[0].imshow(gambar_array)
axs[0].axis('off')
axs[0].set_title('Gambar Asli')

# Contoh pengolahan citra sederhana: Merubah ke citra keabuan (grayscale)
gambar_keabuan = cv2.cvtColor(gambar_array, cv2.COLOR_BGR2GRAY)

# Menampilkan gambar keabuan di subplot kedua
axs[1].imshow(gambar_keabuan, cmap='gray')
axs[1].axis('off')
axs[1].set_title('Gambar Keabuan')

# Menyusun subplot secara horizontal
plt.show()
