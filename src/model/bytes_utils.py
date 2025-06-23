class BytesUtils:
    @staticmethod
    def bin_to_bytes(bin_data: str, reverse_bits: bool = False) -> bytes:
        if not all(digit in "01" for digit in bin_data):
            raise ValueError("Binary string must contain only '0' and '1'")

        return BytesUtils.int_to_bytes(BytesUtils.bin_to_int(bin_data, reverse_bits))

    @staticmethod
    def bin_to_int(bin_data: str, reverse_bits: bool = False) -> int:
        if not all(digit in "01" for digit in bin_data):
            raise ValueError("Binary string must contain only '0' and '1'")

        bitorder = -1 if reverse_bits else 1
        return int(bin_data[::bitorder], 2)

    @staticmethod
    def bytes_to_bin(
        data: bytes, reverse_bytes: bool = False, reverse_bits: bool = False
    ) -> str:
        if not data:
            raise ValueError("Data empty")

        byteorder = -1 if reverse_bytes else 1
        bin_data = ""
        for byte in data[::byteorder]:
            bin_data += f"{byte:08b}"

        bitorder = -1 if reverse_bits and not reverse_bytes else 1
        return bin_data[::bitorder]

    @staticmethod
    def bytes_to_hex(data: bytes, reverse_bytes: bool = False) -> str:
        if not data:
            raise ValueError("Data empty")

        byteorder = -1 if reverse_bytes else 1
        hex_data = ""
        for byte in data[::byteorder]:
            hex_data += f"{byte:02x}"
        return hex_data

    @staticmethod
    def bytes_to_int(data: bytes, reverse_bytes: bool = False) -> int:
        if not data:
            raise ValueError("Data empty")

        byteorder = "little" if reverse_bytes else "big"
        return int.from_bytes(data, byteorder=byteorder)

    @staticmethod
    def int_to_bytes(num: int, reverse_bytes: bool = False) -> bytes:
        byteorder = "little" if reverse_bytes else "big"
        length = (num.bit_length() + 7) // 8 or 1
        return num.to_bytes(length, byteorder=byteorder)
