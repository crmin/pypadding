from math import ceil
from os import urandom

from pypadding.base import BaseEncoder


class Encoder(BaseEncoder):    
    def encode(self, src):
        src_len = len(src)
        block_number = ceil((src_len+1)/self.block_size)
        pad_size = block_number * self.block_size - src_len
        return src + urandom(pad_size-1) + bytes([pad_size])

    def decode(self, encoded_bytes):
        pad_size = encoded_bytes[-1]
        return encoded_bytes[:-pad_size]
