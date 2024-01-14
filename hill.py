import numpy as np

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

def main():
    text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
    n = int(input("Masukkan ukuran matriks kunci (contoh: untuk matriks 2x2, masukkan 2): "))
    key_matrix = []
    print(f"Masukkan {n} baris matriks kunci (tiap baris dengan {n} angka, dipisahkan oleh spasi):")
    for _ in range(n):
        row = list(map(int, input().split()))
        key_matrix.append(row)
    key_matrix = np.array(key_matrix)

    mode = input("Pilih mode ('encrypt' atau 'decrypt'): ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Mode tidak valid. Harap pilih 'encrypt' atau 'decrypt'.")
        return

    result = hill_cipher(text, key_matrix, mode)
    print(f"Hasil {mode}ion: {result}")

if __name__ == "__main__":
    main()
