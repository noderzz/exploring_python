import argparse

#Create the "ArgumentParser" object and save it as "parser"
parser = argparse.ArgumentParser()
parser.add_argument('--input_file', help='Path to input file.')
args = parser.parse_args()

print(f"Input file is {args.input_file}")