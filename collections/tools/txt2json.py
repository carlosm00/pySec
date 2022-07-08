"""
    Title: TXT2JSON (converter)
    Author: Carlos Mena
    Version: 1.0
    Description: CLI python script used for .txt input and json output.
    No debugging, only 1 JSON level output (not nested content).

"""

import json
import sys

# Output file set
input = sys.argv[1]
input_name = input.rsplit("\\")[-1]
output_file = input.replace(".txt", ".json")


# Function for conversion
def converter(input):

    output = open(output_file, "w")
    dict = []

    with open(input) as file:
        for line in file:
            new_line = str(line.strip().split(None, 1))
            dict.append(new_line)

    json.dump(dict, output, indent=4, sort_keys=False)
    output.close()


if __name__ == "__main__":
    converter(input)
