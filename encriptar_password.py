from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

def encrypt_data(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted_data

def decrypt_data(key, encrypted_data):
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
    return decrypted_data

# Generar una clave aleatoria de 16 bytes (128 bits) para el cifrado AES
key = get_random_bytes(16)

# Datos a encriptar
data_to_encrypt = b'Sensitive information'

# Encriptar los datos
encrypted_data = encrypt_data(key, data_to_encrypt)
print("Datos encriptados:", encrypted_data)

# Desencriptar los datos
decrypted_data = decrypt_data(key, encrypted_data)
print("Datos desencriptados:", decrypted_data.decode())
