import unittest
import sys
import os
from context import *
from envedit.parsing import parse_var_list

import os
cwd = os.path.dirname(os.path.realpath(__file__))

class ParseTest(unittest.TestCase):
    def test_var_list(self):
        self.assertEqual(parse_var_list("test"), ["test"])
        in1 = "PATH,LD_LIBRARY_PATH"
        self.assertEqual(parse_var_list(in1), ["PATH", "LD_LIBRARY_PATH"])
if __name__ == '__main__':
    unittest.main()