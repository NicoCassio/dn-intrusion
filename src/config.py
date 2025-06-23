from Crypto.Cipher import AES

IV_SIZE = AES.block_size
KEY = b"abcdefghijklmnop"
CIPHER_MODE = AES.MODE_CFB
