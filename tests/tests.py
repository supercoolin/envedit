import unittest
import sys
import os
from context import *
from envedit.parsing import parse_var_list, parse_path_list
from envedit.common import path_list_to_str
from envedit.env_var import EnvVar

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


class EnvVarTest(unittest.TestCase):
    def test_init(self):
        os.environ["ENVEDIT_TEST_PATH"] = "env:/edit:test"
        inst = EnvVar("ENVEDIT_TEST_PATH")
        self.assertIsNotNone(inst.value)
        self.assertEqual(inst.value, ["env", "/edit", "test"])

    def test_init_bad(self):
        with self.assertRaises(ValueError):
            EnvVar("I want coffee")

    def test_set_value(self):
        os.environ["ENVEDIT_TEST_PATH"] = "env:/edit:test"
        inst = EnvVar("ENVEDIT_TEST_PATH")
        self.assertIsNotNone(inst)
        inst.set_path_list(["/dev/null", "/tmp"])
        self.assertEqual(inst.value, ["/dev/null", "/tmp"])

    def test_get_export(self):
        os.environ["ENVEDIT_TEST_PATH"] = "env:/edit:test"
        inst = EnvVar("ENVEDIT_TEST_PATH")
        self.assertIsNotNone(inst)
        self.assertEqual(inst.get_export(), 'export ENVEDIT_TEST_PATH="env:/edit:test"')

    def test_set_path_list(self):
        os.environ["ENVEDIT_TEST_PATH"] = "env:/edit:test"
        inst = EnvVar("ENVEDIT_TEST_PATH")
        self.assertIsNotNone(inst)
        inst.set_path_list(["/dev/null", "/tmp"])
        self.assertEqual(inst.value, ["/dev/null", "/tmp"])

    def test_remove(self):
        os.environ["ENVEDIT_TEST_PATH"] = "env:/edit:test"
        inst = EnvVar("ENVEDIT_TEST_PATH")
        self.assertIsNotNone(inst)
        inst.remove_val(0)
        self.assertEqual(inst.value, ["/edit", "test"])

    def test_match_env_var(self):
        os.environ["ENVEDIT_TEST_PATH"] = "env:/edit:test"
        inst = EnvVar("ENVEDIT_TEST_PATH")
        self.assertIsNotNone(inst)
        self.assertEqual(inst.match_pattern("env"), 0)
        self.assertEqual(inst.match_pattern("*edit"), 1)
        self.assertIsNone(inst.match_pattern("coffee"))


if __name__ == "__main__":
    unittest.main()
