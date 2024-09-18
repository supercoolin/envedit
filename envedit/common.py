from typing import List, Tuple, Dict, Union

# types
var_list_t = List[str]
path_list_t = List[str]
# functions


def path_list_to_str(path: path_list_t) -> str:
    """convert path list to string
    @param path: path list
    @return: string
    """
    return ":".join(path)
