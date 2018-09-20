from math import ceil

from pypadding.base import BaseEncoder


class Encoder(BaseEncoder):
    def encode(self, src):
        src_len = len(src)
        block_number = ceil((src_len+1)/self.block_size)
        pad_size = block_number * self.block_size - src_len
        return src + b'\x80' + bytes([0] * (pad_size-1))

    def decode(self, encoded_bytes):
        for idx, byte in enumerate(reversed(encoded_bytes)):
            pad_size = 0
            if bytes([byte]) == b'\x80':
                pad_size = idx+1
                break
        return encoded_bytes[:-pad_size]
