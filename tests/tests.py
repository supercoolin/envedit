import unittest
import sys
import os
from context import *
from envedit.parsing import parse_var_list

import os
cwd = os.path.dirname(os.path.realpath(__file__))

class ParseTest(unittest.TestCase):
    def test_single_val(self):
        self.assertEqual(parse_var_list("test"), ["test"])
if __name__ == '__main__':
    unittest.main()