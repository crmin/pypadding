import unittest


loader = unittest.TestLoader()
suite = loader.discover('pypadding.tests')

runner = unittest.TextTestRunner()
runner.run(suite)
