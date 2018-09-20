import os
import sys
import unittest

FILE_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(FILE_DIR, '..', '..')
sys.path.append(ENV_PATH)

from pypadding import iso7816_4


class ISO7816_4Tests(unittest.TestCase):
    def setUp(self):
        self.encoder = iso7816_4.Encoder()

    def test_encode_src_is_blank(self):
        src = b''
        right_ans = b'\x80\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(self.encoder.encode(src), right_ans)

    def test_encode_src_len_smaller_than_block_size(self):
        src = b'hello'
        right_ans = b'hello\x80\x00\x00'
        self.assertEqual(self.encoder.encode(src), right_ans)

    def test_encode_src_len_equal_to_block_size(self):
        src = b'computer'
        right_ans = b'computer\x80\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(self.encoder.encode(src), right_ans)

    def test_encode_src_len_bigger_than_block_size_and_smaller_than_2x_block_size(self):
        src = b'blackjack'
        right_ans = b'blackjack\x80\x00\x00\x00\x00\x00\x00'
        self.assertEqual(self.encoder.encode(src), right_ans)

    def test_encode_src_len_equal_to_2x_block_size(self):
        src = b'hydroelectricity'
        right_ans = b'hydroelectricity\x80\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(self.encoder.encode(src), right_ans)

    def test_decode_src_is_blank(self):
        src = b'\x80\x00\x00\x00\x00\x00\x00\x00'
        right_ans = b''
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_smaller_than_block_size(self):
        src = b'hello\x80\x00\x00'
        right_ans = b'hello'
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_equal_to_block_size(self):
        src = b'computer\x80\x00\x00\x00\x00\x00\x00\x00'
        right_ans = b'computer'
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_bigger_than_block_size_and_smaller_than_2x_block_size(self):
        src = b'blackjack\x80\x00\x00\x00\x00\x00\x00'
        right_ans = b'blackjack'
        self.assertEqual(self.encoder.decode(src), right_ans)

    def test_decode_src_len_equal_to_2x_block_size(self):
        src = b'hydroelectricity\x80\x00\x00\x00\x00\x00\x00\x00'
        right_ans = b'hydroelectricity'
        self.assertEqual(self.encoder.decode(src), right_ans)
