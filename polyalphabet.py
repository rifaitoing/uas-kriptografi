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

if __name__ == "__main__":
    main()
