import os
from .common import path_list_t, path_list_to_str
from .parsing import parse_path_list
class EnvVar:
    """
    This class holds information about an environment variable
    currently supports reading from the current environment variables and exporting new ones
    """
    def __init__(self, name: str, get_val: bool=True) -> None:
        """ Constructor 
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
        """ Loads the value from the current environment variables
        @note: This assumes that the current value represents a path list
        """
        value = os.environ[self.name]
        self.value = parse_path_list(value)

    def get_export(self):
        return f'export {self.name}="{path_list_to_str(self.value)}"'
    
    def set_path_list(self, path: path_list_t) -> None:
        """ Sets the value of this environment variable to a list of paths
        @param path: the new value for this environment variable
        """
        self.value = path
