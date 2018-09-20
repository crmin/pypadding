from os import urandom
import unittest

from pypadding import iso10126


class ISO10126Tests(unittest.TestCase):
    def setUp(self):
        self.encoder = iso10126.Encoder()

    def _change_random_bytes_to_x(self, data):
        padding_bytes_num = data[-1]
        return data[:-padding_bytes_num] + ('x'*(padding_bytes_num-1)).encode() + bytes([padding_bytes_num])

    def test_encode_src_is_blank(self):
        src = b''
        right_ans = b'xxxxxxx\x08'
        self.assertEqual(self._change_random_bytes_to_x(self.encoder.encode(src)), right_ans)

    def test_encode_src_len_smaller_than_block_size(self):
        src = b'hello'
        right_ans = b'helloxx\x03'
        self.assertEqual(self._change_random_bytes_to_x(self.encoder.encode(src)), right_ans)

    def test_encode_src_len_equal_to_block_size(self):
        src = b'computer'
        right_ans = b'computerxxxxxxx\x08'
        self.assertEqual(self._change_random_bytes_to_x(self.encoder.encode(src)), right_ans)

    def test_encode_src_len_bigger_than_block_size_and_smaller_than_2x_block_size(self):
        src = b'blackjack'
        right_ans = b'blackjackxxxxxx\x07'
        self.assertEqual(self._change_random_bytes_to_x(self.encoder.encode(src)), right_ans)

    def test_encode_src_len_equal_to_2x_block_size(self):
        src = b'hydroelectricity'
        right_ans = b'hydroelectricityxxxxxxx\x08'
        self.assertEqual(self._change_random_bytes_to_x(self.encoder.encode(src)), right_ans)

    def test_decode_src_is_blank(self):
        src = urandom(7) + b'\x08'
        right_ans = b''
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_smaller_than_block_size(self):
        src = b'hello' + urandom(2) + b'\x03'
        right_ans = b'hello'
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_equal_to_block_size(self):
        src = b'computer' + urandom(7) + b'\x08'
        right_ans = b'computer'
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_bigger_than_block_size_and_smaller_than_2x_block_size(self):
        src = b'blackjack' + urandom(6) + b'\x07'
        right_ans = b'blackjack'
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_equal_to_2x_block_size(self):
        src = b'hydroelectricity' + urandom(7) + b'\x08'
        right_ans = b'hydroelectricity'
        self.assertEqual(self.encoder.decode(src), right_ans)
