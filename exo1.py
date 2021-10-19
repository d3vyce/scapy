import ieee
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("mac")
args = parser.parse_args()

print("Searching:", args.mac)


ieee_parser = ieee.IEEEParser()
result = ieee_parser.search_constructor(args.mac)

if (result):
    print("Constructor found:", result)
else:
    print("No constructor found")