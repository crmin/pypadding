class BaseEncoder():
    def __init__(self, block_size=8):  # blowfish=8, aes=16
        self.block_size = block_size
