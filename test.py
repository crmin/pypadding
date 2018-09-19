import os
import sys
import unittest


FILE_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(FILE_DIR, '..')
sys.path.append(ENV_PATH)

loader = unittest.TestLoader()
suite = loader.discover('pypadding.tests')

runner = unittest.TextTestRunner()
runner.run(suite)
