from stegano import lsb

# Path to the image with hidden text
path_gambar = r"D:/semester 5/kriptografi/perruang.png"

# Reveal the hidden message from the image
revealed_message = lsb.reveal(path_gambar)

# Print the revealed message
print("Revealed Message:", revealed_message)
