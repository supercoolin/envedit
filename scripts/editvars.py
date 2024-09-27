#!/bin/python
import argparse
import envedit
import sys
from typing import List

warn = "#WARNING:"
ACTION_LIST_FILTER = "list_filter"
ACTION_LIST_REPLACE = "list_replace"


def parse_vars(variables) -> List[envedit.EnvVar]:
    var_list = envedit.parse_var_list(variables)
    parsed = []
    for v in var_list:
        try:
            envar = envedit.EnvVar(v)
        except ValueError as e:
            print(f"Could not find environment variable: {v}", file=sys.stderr)
            exit(1)
        parsed.append(envar)
    return parsed


def var_list_export(envVars: List[envedit.EnvVar]):
    return "\n".join([v.get_export() for v in envVars])


def handle_output(result: str, args):
    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
    else:
        print(result)


def list_filter(args):
    envVars = parse_vars(args.variables)
    for v in envVars:
        if v.match_pattern(args.pattern) is None:
            print(f"{warn} Pattern {args.pattern} not found in variable {v.name}")
        while idx := v.match_pattern(args.pattern):
            v.remove_val(idx)
    handle_output(var_list_export(envVars), args)


def list_replace(args):
    envVars = parse_vars(args.variables)
    n_replace = args.max
    for v in envVars:
        while idx := v.match_pattern(args.pattern):
            if n_replace and n_replace <= 0:
                break
            v.replace_val(idx, args.value)
            if n_replace:
                n_replace -= 1
    handle_output(var_list_export(envVars), args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument(
        "variables", help="comma separated list of environment variables to affect"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file name, if absent, the program will print to stdout.",
    )
    action_parsers = parser.add_subparsers(
        help="Action to be performed on the environment variables", required=True
    )

    list_filter_parser = action_parsers.add_parser(
        ACTION_LIST_FILTER,
        help="filter out the elements from the colon separated lists.",
    )
    list_filter_parser.set_defaults(func=list_filter)

    list_filter_parser.add_argument(
        "pattern", help="The pattern to filter out. Supports Unix style globs."
    )

    list_replace_parser = action_parsers.add_parser(
        ACTION_LIST_REPLACE,
        help="Replace the elements from the colon separated lists.",
    )
    list_replace_parser.set_defaults(func=list_replace)
    list_replace_parser.add_argument("pattern", help="The pattern to replace.")
    list_replace_parser.add_argument("value", help="The value to replace with.")
    list_replace_parser.add_argument(
        "-m",
        "--max",
        action="store",
        help="Maximum number of times to replace the pattern. If absent, replaces every instance.",
        type=int,
    )

    args = parser.parse_args()
    args.func(args)

    exit(0)
