import time

from src.config import ACK_SIZE, COMMANDS, IV_SIZE, SIMPLE_COMMANDS
from src.model.bytes_utils import BytesUtils
from src.model.serial_communicator import SerialCommunicator


class Model:
    def __init__(self) -> None:
        self._serial_communicator = SerialCommunicator()

    def send_command(self, command: str) -> None:
        if command not in COMMANDS:
            raise ValueError(f"{command} is not a valid command.")

        self._command = command
        self._serial_communicator.write(self._command.encode())
        self._ack = self._read_ack()
        if self._command not in SIMPLE_COMMANDS:
            self._handle()

    def _read_ack(self) -> bytes:
        if self._command in ["C03"]:
            self._serial_communicator.set_timeout(3)

        ack = self._serial_communicator.read(IV_SIZE + ACK_SIZE)
        self._serial_communicator.set_timeout()

        if ack[:3] != self._command.replace("C", "R").encode():
            raise ValueError("Wrong answer.")

        return ack

    def _handle(self) -> None:
        match self._command:
            case "C06":
                self._serial_communicator.write(
                    BytesUtils.int_to_bytes(int(time.time()), reverse_bytes=True)
                )
                if self._read_ack() != b"R06OK":
                    raise ValueError("Wrong Answer.")
                return
            case "C08":
                ...
