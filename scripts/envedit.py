#!/bin/python
import argparse
def main():
    return "Test went well !"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument("variables", help="comma separated list of environment variables to affect")
    parser.add_argument("-o", "--output", help="output file name, if absent, the program will print to stdout.")
    action_parsers = parser.add_subparsers(help="Action to be performed on the environment variables", required=True)

    list_filter_parser = action_parsers.add_parser("list_filter", help="filter out the elements from the colon separated lists.")

    args = parser.parse_args()
    res = main()
    if args.output:
        with open(args.output, "w") as f:
            f.write(res)
    else:
        print(res)
    exit(0)