import argparse

#Create the "ArgumentParser" object and save it as "parser"
parser = argparse.ArgumentParser()

#Set the flag for the input file along with the help information.
parser.add_argument('-i', '--input_file', help='Path to input file.')

#Make it so I can access the parsed objects as variables.
args = parser.parse_args()

#Print off the parsed object variable
print(f"Input file is {args.input_file}")