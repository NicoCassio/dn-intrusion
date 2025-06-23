from Crypto import Random
from Crypto.Cipher import AES

from src.config import CIPHER_MODE, IV_SIZE, KEY


class CryptoHandler:
    @staticmethod
    def decrypt(data: bytes) -> bytes:
        if len(data) < IV_SIZE:
            raise ValueError(f"Data must be at least {IV_SIZE} bytes long.")

        iv = data[:IV_SIZE]
        cipher = AES.new(KEY, CIPHER_MODE, iv)
        return cipher.decrypt(data[IV_SIZE:])

    @staticmethod
    def encrypt(data: bytes) -> bytes:
        iv = Random.new().read(IV_SIZE)
        cipher = AES.new(KEY, CIPHER_MODE, iv)
        return iv + cipher.encrypt(data)
