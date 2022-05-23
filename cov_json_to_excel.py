import pandas as pd
import json
import argparse

parser = argparse.ArgumentParser(description='Convert a Coverity json file with stats to an Excel file.')
parser.add_argument('input_file_name', help='the json file from Coverity')
parser.add_argument('--output_file_name', '-o', help='the Excel file to write', default='output.xlsx')
args = parser.parse_args()

input_file_name = args.input_file_name
output_file_name = args.output_file_name

with open(input_file_name, 'r') as file:
    data = json.load(file)

frames = {}

for section_name, section in data.items():
    df = pd.DataFrame(section)
    frames[section_name] = df

with pd.ExcelWriter(output_file_name) as writer:
    for section_name, frame in frames.items():
        frame.to_excel(writer, sheet_name=section_name, index=False)
