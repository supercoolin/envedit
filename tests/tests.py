import unittest
import sys
import os
from context import *
from envedit.parsing import parse_var_list, parse_path_list
from envedit.common import path_list_to_str

import os
cwd = os.path.dirname(os.path.realpath(__file__))

class ParseTest(unittest.TestCase):

    def test_var_list(self):
        self.assertEqual(parse_var_list("test"), ["test"])
        in1 = "PATH,LD_LIBRARY_PATH"
        self.assertEqual(parse_var_list(in1), ["PATH", "LD_LIBRARY_PATH"])

    def test_path_list(self):
        self.assertEqual(parse_path_list("test"), ["test"])
        in1 = "/dev/null:/tmp"
        self.assertEqual(parse_path_list(in1), ["/dev/null", "/tmp"])

class CommonTest(unittest.TestCase):

    def test_path_list_to_str(self):
        
        self.assertEqual(path_list_to_str(["/dev/null", "/tmp"]), "/dev/null:/tmp")
        self.assertEqual(path_list_to_str(["root"]), "root")
        self.assertEqual(path_list_to_str([]), "")


if __name__ == '__main__':
    unittest.main()