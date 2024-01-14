from PIL import Image

def hide_text(image_path, secret_text, output_path):
    img = Image.open(image_path)
    img = img.convert('RGBA')

    secret_data = bytearray(secret_text, 'utf-8')

    data_index = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if data_index < len(secret_data):
                pixel = list(img.getpixel((x, y)))
                for i in range(3):
                    pixel[i] = (pixel[i] & 0xFE) | ((secret_data[data_index] >> 7 - i) & 1)
                img.putpixel((x, y), tuple(pixel))
                data_index += 1
            else:
                break

    img.save(output_path)

# Pilih gambar dari perangkat Anda
uploaded_image = files.upload()

# Pilih teks yang ingin Anda sembunyikan
secret_text = input("Masukkan teks yang ingin Anda sembunyikan: ")

# Sembunyikan teks dalam gambar
for image_path in uploaded_image.keys():
    output_path = f"hidden_{image_path}"
    hide_text(image_path, secret_text, output_path)
    print(f"Teks telah disembunyikan dalam gambar {image_path}. Simpan dengan nama {output_path}.")

# Unduh gambar yang telah dimodifikasi
files.download(output_path)
