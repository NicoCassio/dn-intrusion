from src.model.encryption import CryptoHandler


def test_encryption() -> None:
    data = b"test"
    encrypted_data = CryptoHandler.encrypt(data)
    decrypted_data = CryptoHandler.decrypt(encrypted_data)
    assert decrypted_data == data
