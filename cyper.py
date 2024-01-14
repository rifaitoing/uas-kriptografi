import string
import numpy as np

#Affine ciper
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_cipher(text, key, mode):
    result = ""
    a, b = key
    if mode == "encrypt":
        for char in text:
            if char in string.ascii_letters:
                if char.islower():
                    result += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
                else:
                    result += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            else:
                result += char
    elif mode == "decrypt":
        a_inv = mod_inverse(a, 26)
        if a_inv is None:
            return "Key is not valid for decryption"
        for char in text:
            if char in string.ascii_letters:
                if char.islower():
                    result += chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
                else:
                    result += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
            else:
                result += char
    return result
#caesar
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

def main():
    text = input("Masukkan teks yang ingin dienkripsi: ")
    shift = int(input("Masukkan jumlah pergeseran: "))

    encrypted_text = caesar_cipher(text, shift)
    print("Teks terenkripsi:", encrypted_text)

#vigenere
def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('a')
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            if mode == 'encrypt':
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                shifted_char = chr((ord(char) - base - shift) % 26 + base)

            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
    key = input("Masukkan kunci: ")
    mode = input("Pilih mode ('encrypt' atau 'decrypt'): ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Mode tidak valid. Harap pilih 'encrypt' atau 'decrypt'.")
        return

    result = vigenere_cipher(text, key, mode)
    print(f"Hasil {mode}ion: {result}")

#polyalphabet
def polyalphabetic_cipher(text, keys, mode='encrypt'):
    result = []
    key_count = len(keys)
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = keys[i % key_count][0]  # Mengambil karakter pertama dari setiap kunci
            shift = ord(key_char) - ord('a')
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            if mode == 'encrypt':
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                shifted_char = chr((ord(char) - base - shift) % 26 + base)

            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
    num_keys = int(input("Masukkan jumlah kunci: "))
    keys = []
    for i in range(num_keys):
        key = input(f"Masukkan kunci ke-{i+1}: ")
        keys.append(key)

    mode = input("Pilih mode ('encrypt' atau 'decrypt'): ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Mode tidak valid. Harap pilih 'encrypt' atau 'decrypt'.")
        return

    result = polyalphabetic_cipher(text, keys, mode)
    print(f"Hasil {mode}ion: {result}")

#hill
def matrix_modulo_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inverse = None
    for i in range(modulus):
        if (det * i) % modulus == 1:
            det_inverse = i
            break
    if det_inverse is None:
        raise ValueError("Inverse does not exist for the given matrix and modulus.")
    adjugate = np.round(det * np.linalg.inv(matrix))
    inverse = (det_inverse * adjugate) % modulus
    return inverse.astype(int)

def text_to_matrix(text, n):
    matrix = []
    for char in text:
        if char.isalpha():
            matrix.append(ord(char) - ord('A'))
    while len(matrix) % n != 0:
        matrix.append(0)
    matrix = np.array(matrix)
    return matrix.reshape(len(matrix) // n, n)

def matrix_to_text(matrix):
    text = ""
    for num in matrix.flatten():
        text += chr(num + ord('A'))
    return text

def hill_cipher(text, key_matrix, mode='encrypt'):
    n = key_matrix.shape[0]
    modulus = 26  # Jumlah karakter dalam alfabet Inggris
    if mode == 'encrypt':
        plaintext_matrix = text_to_matrix(text, n)
        ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % modulus
        ciphertext = matrix_to_text(ciphertext_matrix)
        return ciphertext
    elif mode == 'decrypt':
        key_inverse = matrix_modulo_inverse(key_matrix, modulus)
        ciphertext_matrix = text_to_matrix(text, n)
        plaintext_matrix = np.dot(ciphertext_matrix, key_inverse) % modulus
        plaintext = matrix_to_text(plaintext_matrix)
        return plaintext
    else:
        raise ValueError("Mode harus 'encrypt' atau 'decrypt'.")

# Fungsi Playfair Cipher
def prepare_text(text):
    # Hapus karakter non-alfabet dan ubah menjadi huruf besar
    text = ''.join(filter(str.isalpha, text)).upper()
    # Ganti 'J' dengan 'I'
    text = text.replace('J', 'I')
    return text

def create_playfair_table(key):
    # Buat tabel Playfair
    key = prepare_text(key)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Abaikan 'J'
    table = [['' for _ in range(5)] for _ in range(5)]
    used_chars = set()

    row, col = 0, 0

    for char in key:
        if char not in used_chars:
            table[row][col] = char
            used_chars.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1

    for char in alphabet:
        if char not in used_chars:
            table[row][col] = char
            used_chars.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return table

def find_char_location(table, char):
    for i in range(5):
        for j in range(5):
            if table[i][j] == char:
                return (i, j)

def encrypt_playfair(plain_text, key):
    table = create_playfair_table(key)
    plain_text = prepare_text(plain_text)
    cipher_text = ''

    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
        if char1 == char2:
            char2 = 'X'
            i -= 1

        row1, col1 = find_char_location(table, char1)
        row2, col2 = find_char_location(table, char2)

        if row1 == row2:
            cipher_text += table[row1][(col1 + 1) % 5]
            cipher_text += table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += table[(row1 + 1) % 5][col1]
            cipher_text += table[(row2 + 1) % 5][col2]
        else:
            cipher_text += table[row1][col2]
            cipher_text += table[row2][col1]

        i += 2

    return cipher_text

def decrypt_playfair(cipher_text, key):
    table = create_playfair_table(key)
    plain_text = ''

    i = 0
    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]

        row1, col1 = find_char_location(table, char1)
        row2, col2 = find_char_location(table, char2)

        if row1 == row2:
            plain_text += table[row1][(col1 - 1) % 5]
            plain_text += table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += table[(row1 - 1) % 5][col1]
            plain_text += table[(row2 - 1) % 5][col2]
        else:
            plain_text += table[row1][col2]
            plain_text += table[row2][col1]

        i += 2

    return plain_text

# Fungsi Main
def main():
    while True:
        print("Pilih cipher yang ingin Anda gunakan:")
        print("1. Caesar Cipher")
        print("2. Vigenere Cipher")
        print("3. Polyalphabet Cipher")
        print("4. Hill Cipher")
        print("5. Playfair Cipher")
        print("6. Affine Cipher")
        print("7. Keluar")

        choice = input("Masukkan nomor pilihan (1/2/3/4/5/6/7): ")

        if choice == '1':
            text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
            shift = int(input("Masukkan jumlah pergeseran: "))
            encrypted_text = caesar_cipher(text, shift)
            print("Teks terenkripsi:", encrypted_text)

        elif choice == '2':
            text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
            key = input("Masukkan kunci: ")
            mode = input("Pilih mode ('encrypt' atau 'decrypt'): ").lower()
            result = vigenere_cipher(text, key, mode)
            print(f"Hasil {mode}ion: {result}")

        elif choice == '3':
            text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
            num_keys = int(input("Masukkan jumlah kunci: "))
            keys = []
            for i in range(num_keys):
                key = input(f"Masukkan kunci ke-{i + 1}: ")
                keys.append(key)
            mode = input("Pilih mode ('encrypt' atau 'decrypt'): ").lower()
            result = polyalphabetic_cipher(text, keys, mode)
            print(f"Hasil {mode}ion: {result}")

        elif choice == '4':
            text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
            n = int(input("Masukkan ukuran matriks kunci (contoh: untuk matriks 2x2, masukkan 2): "))
            key_matrix = []
            print(f"Masukkan {n} baris matriks kunci (tiap baris dengan {n} angka, dipisahkan oleh spasi):")
            for _ in range(n):
                row = list(map(int, input().split()))
                key_matrix.append(row)
            key_matrix = np.array(key_matrix)
            mode = input("Pilih mode ('encrypt' atau 'decrypt'): ").lower()
            result = hill_cipher(text, key_matrix, mode)
            print(f"Hasil {mode}ion: {result}")

        elif choice == '5':
            key = input("Masukkan kunci Playfair: ")
            plaintext = input("Masukkan teks plaintext: ")
            encrypted_text = encrypt_playfair(plaintext, key)
            decrypted_text = decrypt_playfair(encrypted_text, key)
            print("Plaintext: ", plaintext)
            print("Encrypted: ", encrypted_text)
            print("Decrypted: ", decrypted_text)

        elif choice == '6':
            text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
            a = int(input("Masukkan nilai 'a' (integer): "))
            b = int(input("Masukkan nilai 'b' (integer): "))
            key = (a, b)
            mode = input("Encrypt (e) atau Decrypt (d)?: ").lower()

            if mode == "e":
                mode = "encrypt"
            elif mode == "d":
                mode = "decrypt"

            result = affine_cipher(text, key, mode)
            print(f"{mode.capitalize()}ed Text: {result}")

        elif choice == '7':
            break  # Keluar dari program

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
