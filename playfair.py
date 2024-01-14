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

# Input teks dari pengguna
key = input("Masukkan kunci: ")
plaintext = input("Masukkan teks plaintext: ")

encrypted_text = encrypt_playfair(plaintext, key)
decrypted_text = decrypt_playfair(encrypted_text, key)

print("Plaintext: ", plaintext)
print("Encrypted: ", encrypted_text)
print("Decrypted: ",decrypted_text)