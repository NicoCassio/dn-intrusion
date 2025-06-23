from serial import Serial

from src.config import BAUDRATE, TIMEOUT
from src.model.crypto_handler import CryptoHandler


class SerialCommunicator:
    def __init__(self, port: str | None = None) -> None:
        self._serial = Serial(port, baudrate=BAUDRATE, timeout=TIMEOUT)

    def connect(self, port: str | None = None) -> None:
        self._serial.port = port
        self._serial.open()

    def discnonect(self) -> None:
        self._serial.close()

    def is_connected(self) -> bool:
        return self._serial.is_open

    def read(self, size: int, encrypted: bool = True) -> bytes:
        data = self._serial.read(size)
        if encrypted:
            data = CryptoHandler.decrypt(data)

        return data

    def set_timeout(self, timeout: int | None = None) -> None:
        self._serial.timeout = timeout if timeout else TIMEOUT

    def write(self, data: bytes, encrypted: bool = True) -> None:
        if encrypted:
            data = CryptoHandler.encrypt(data)

        self._serial.write(data)
