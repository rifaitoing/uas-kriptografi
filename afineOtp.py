import pyotp

# Membuat secret key (dapat di-generate satu kali dan disimpan aman)
secret_key = pyotp.random_base32()

# Membuat instance TOTP dengan secret key
totp = pyotp.TOTP(secret_key)

# Mendapatkan OTP
otp = totp.now()
print("One-Time Password:", otp)
