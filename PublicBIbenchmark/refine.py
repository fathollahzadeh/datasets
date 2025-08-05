import csv
import json
from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, default=None)
    parser.add_argument('--dataset-name', type=str, default=None)

    args = parser.parse_args()
    
    return args

def fix_quotes_in_field(field):
    # Remove stray unmatched quotes or escape them
    if field.count('"') % 2 != 0:
        field = field.replace('"', '')  # or use escaping if preferred
    return field

def clean_field(field, idx):
    field = field.strip()

    # if idx in json_fields:
    #     # escape pipe characters and fix quotes inside JSON
    #     field = field.replace('|', '&#124;')
    #     field = fix_quotes_in_field(field)
    #     return field

    # General field handling
    # field = field.replace('|', '&#124;')
    field = fix_quotes_in_field(field)
    return field

if __name__ == '__main__':
    args = parse_arguments()
    print(args)
    input_file = args.data_path
    output_file = f'{input_file}_clean'
    expected_cols = {'HashTags': 101, 'Corporations': 27, 'Euro2016': 11, 'IGlocations2': 20,'Rentabilidad': 0,'Romance': 12,'TableroSistemaPenal': 0, 'NYC': 54}
    if args.dataset_name == "Rentabilidad":
        if "Rentabilidad_2.csv" in input_file:
            expected_columns = 138
        else :
            expected_columns = 141
    elif args.dataset_name == "TableroSistemaPenal":
        if "TableroSistemaPenal_1.csv" in input_file:
            expected_columns = 27
        elif "TableroSistemaPenal_2.csv" in input_file:
            expected_columns = 22
        elif "TableroSistemaPenal_3.csv" in input_file:
            expected_columns = 21
        elif "TableroSistemaPenal_4.csv" in input_file:
            expected_columns = 21
        elif "TableroSistemaPenal_5.csv" in input_file:
            expected_columns = 21
        elif "TableroSistemaPenal_6.csv" in input_file:
            expected_columns = 13
        elif "TableroSistemaPenal_7.csv" in input_file:
            expected_columns = 27
        elif "TableroSistemaPenal_8.csv" in input_file:
            expected_columns = 22            
    else:
         expected_columns = expected_cols[args.dataset_name]

    with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        writer = csv.writer(outfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar='\\')

        for line_number, line in enumerate(infile, 1):
            # Try parsing the line as CSV
            line = line.replace('"', "'")
            try:
                # Try splitting the line as CSV, even with broken quotes
                row = next(csv.reader([line], delimiter='|', quotechar='"', escapechar='\\'))

                # Fix quote issues in each field
                cleaned = [clean_field(f, i) for i, f in enumerate(row)]

                if len(cleaned) != expected_columns:
                    print(f"Line {line_number}: Skipped (got {len(cleaned)} columns)")                    
                    continue

                writer.writerow(cleaned)

            except Exception as e:
                print(f"Line {line_number}: Parse error — {e}")