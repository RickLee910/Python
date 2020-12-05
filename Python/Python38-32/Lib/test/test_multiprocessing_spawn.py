import unittest
from spider import test

from spider.test import support

if support.PGO:
    raise unittest.SkipTest("test is not helpful for PGO")

test._test_multiprocessing.install_tests_in_module_dict(globals(), 'spawn')

if __name__ == '__main__':
    unittest.main()
