import os
from .common import path_list_t, path_list_to_str
from .parsing import parse_path_list
import fnmatch


class EnvVar:
    """
    This class holds information about an environment variable
    currently supports reading from the current environment variables and exporting new ones
    """

    def __init__(self, name: str, get_val: bool = True) -> None:
        """Constructor
        @param name: the name of the environment variable
        @param get_val: whether to get the value of the environment variable from the current environment
        """
        self.name = name
        if not self.name in os.environ:
            raise ValueError(f"Environment variable {name} not found")
        if get_val:
            self.load_from_env()
        else:
            self.value = ""

    def load_from_env(self):
        """Loads the value from the current environment variables
        @note: This assumes that the current value represents a path list
        """
        value = os.environ[self.name]
        self.value = parse_path_list(value)

    def get_export(self):
        return f'export {self.name}="{path_list_to_str(self.value)}"'

    def set_path_list(self, path: path_list_t) -> None:
        """Sets the value of this environment variable to a list of paths
        @param path: the new value for this environment variable
        """
        self.value = path

    def match_pattern(self, pattern: str):
        """
        Returns the index of the value of this variable matches the given pattern
        @param pattern: the pattern to match
        @return int: index of the value that matches
        """
        for i, val in enumerate(self.value):
            if fnmatch.fnmatch(val, pattern):
                return i

    def remove_val(self, index: int):
        """
        Removes a value from the list at the given index
        @param index: the index of the value to remove
        """
        self.value = self.value[:index] + self.value[index + 1 :]

    def replace_val(self, index: int, val: str):
        """
        Replaces a value from the list at the given index
        @param index: the index of the value to replace
        @param val: the new value to insert
        """
        self.value[index] = val
