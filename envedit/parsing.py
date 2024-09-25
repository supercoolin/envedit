from .common import var_list_t, path_list_t


def parse_var_list(vars_in: str) -> var_list_t:
    """
    Parses a list of environment variables from strings in the following format
    <env_var> | <env_var>,<env_var>,<...>
    @param vars_in(str): the string to parse into a variable list
    @return (var_list_t): the parsed variable list
    """
    if "," not in vars_in:
        return [vars_in]
    else:
        return vars_in.split(",")


def parse_path_list(vars_in: str) -> path_list_t:
    """
    Parses a path list in a classic colon separated list
    <path> | <path>:<path>:<...>
    @param vars_in(str): the string to parse into a path list
    @return (path_list_t):
    """
    if ":" not in vars_in:
        return [vars_in]
    else:
        return vars_in.split(":")
