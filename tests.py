import os
import sys
import unittest

loader = unittest.TestLoader()
suite = loader.discover('tests')

runner = unittest.TextTestRunner()
runner.run(suite)
