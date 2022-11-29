INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"


def csv_to_list_dict(filename, filename2, delimiter=',', newline='\n', indent='     '):
    with open(filename) as input_file:
        with open(filename2, 'w') as output_file:
            output_file.write('[')
            headings = input_file.readline().replace('\n', "").split(delimiter)
            for count, line in enumerate(input_file):
                input_line = line.replace('\n', "").split(newline)
                for current_line in input_line:
                    json_line = dict(zip(headings, current_line.split(delimiter)))
                    dict_delimiter = "" if count == 0 else delimiter
                    output_file.write(dict_delimiter + newline + indent + '{')
                    fist_row = True
                    for key, value in json_line.items():
                        row_delimiter = "" if fist_row else delimiter
                        output_file.write(row_delimiter + newline + f'{indent}{indent}"{key}": {value}')
                        fist_row = False
                    output_file.write(newline + indent + '}')
            output_file.write(newline + ']' + newline)


csv_to_list_dict(INPUT_FILE, OUTPUT_FILE)

