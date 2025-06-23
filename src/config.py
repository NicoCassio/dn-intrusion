from Crypto.Cipher import AES

IV_SIZE = AES.block_size
KEY = b"abcdefghijklmnop"
CIPHER_MODE = AES.MODE_CFB

BAUDRATE = 115200
TIMEOUT = 3

ACK_SIZE = 5

COMMANDS = [
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "C07",
    "C08",
    "C09",
    "C10",
    "C11",
    "C12",
    "C13",
]

SIMPLE_COMMANDS = [
    "C01",
    "C02",
    "C03",
    "C04",
]
