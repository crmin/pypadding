# PyPadding

[![Build Status](https://travis-ci.org/blinglnav/pypadding.svg?branch=master)](https://travis-ci.org/blinglnav/pypadding)

This package implements padding methods to use block crypto function.

## Dependencies

* Python 3+

## Usage

### PKCS#5 / PKCS#7
* pypadding.pkcs
* Fill using number of padding number
* e.g. When block size is 8, b'hello' need 3 bytes to multiple of block size --> fill using `b'\x03'` (`b'hello\x03\x03\x03'`)

```python
>>> from pypadding import pkcs
>>> encoder = pkcs.Encoder()
>>> encoder.encode(b'hello')
b'hello\x03\x03\x03'
>>> encoder.decode(b'hello\x03\x03\x03')
b'hello'
```

### ANSI x923
* pypadding.x923
* Fill using zero(`b'\x00'`) and last byte set to length of padding
* e.g. When block size is 8, b'hello' need 3 bytes to multiple of block size --> fill using `b'\x00'` and last byte set to `b'\x03'` (`b'hello\x00\x00\x03'`)

```python
>>> from pypadding import x923
>>> encoder = x923.Encoder()
>>> encoder.encode(b'hello')
b'hello\x00\x00\x03'
>>> encoder.decode(b'hello\x00\x00\x03')
b'hello'
```

### ISO 10126
* pypadding.iso10126
* Fill using random byte and last byte set to length of padding
* e.g. When block size is 8, b'hello' need 3 bytes to multiple of block size --> fill random byte and last byte set to `b'\x03'` (`b'hello\x85\xaa\x03'`)

```python
>>> from pypadding import iso10126
>>> encoder = iso10126.Encoder()
>>> encoder.encode(b'hello')
b'hello\x85\xaa\x03'
>>> encoder.decode(b'hello\x85\xaa\x03')
b'hello'
```

### ISO/IEC 7816-4
* pypadding.iso7816_4
* Padding starts with `b'\x80'` and fill using zero `b'\x00'`
* e.g. When block size is 8, b'hello' need 3 bytes to multiple of block size --> fill first byte to `b'\x80'` then fill to `b'\x00'` (`b'hello\x80\x00\x00'`)

```python
>>> from pypadding import iso7816_4
>>> encoder = iso7816_4.Encoder()
>>> encoder.encode(b'hello')
b'hello\x80\x00\x00'
>>> encoder.decode(b'hello\x80\x00\x00')
b'hello'
```

## Set Block Size

```python
>>> from pypadding import pkcs
>>> encoder = pkcs.Encoder(16)
>>> encoder.encode(b'blackjack')
b'blackjack\x07\x07\x07\x07\x07\x07\x07'
>>> encoder.decode(b'blackjack\x07\x07\x07\x07\x07\x07\x07')
b'blackjack'
```

or

```python
>>> from pypadding import pkcs
>>> encoder = pkcs.Encoder(block_size=16)
>>> encoder.encode(b'blackjack')
b'blackjack\x07\x07\x07\x07\x07\x07\x07'
>>> encoder.decode(b'blackjack\x07\x07\x07\x07\x07\x07\x07')
b'blackjack'
```


## Note
* All encoded data has padding even though length of original data is multiple of block size
    * e.g. block size = 8, encoding w/ pkcs, `encode('computer')` --> `b'computer\x08\x08\x08\x08\x08\x08\x08\x08'`


## Reference
* https://en.wikipedia.org/wiki/Padding_(cryptography)
    * This package implement reversible methods only
