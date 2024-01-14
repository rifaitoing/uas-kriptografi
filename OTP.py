# Import pyotp
import pyotp

# Membuat secret key (dapat di-generate satu kali dan disimpan aman)
secret_key = pyotp.random_base32()

# Membuat instance TOTP dengan secret key
totp = pyotp.TOTP(secret_key)

# Mendapatkan OTP
otp = totp.now()
print("One-Time Password:", otp)
# Verifikasi OTP
user_input = input("Masukkan OTP yang Anda terima: ")
if totp.verify(user_input):
    print("OTP valid. Akses diberikan.")
else:
    print("OTP tidak valid. Akses ditolak.")
