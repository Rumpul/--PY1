INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"


def csv_to_list_dict(filename, delimiter=',', newline='\n'):
    with open(filename) as input_file:
        headings = input_file.readline().replace('\n', "").split(delimiter)
        for line in input_file:
            input_line = line.replace('\n', "").split(newline)
            for current_line in input_line:
                yield dict(zip(headings, current_line.split(delimiter)))


def json_writer(filename, delimiter=',', newline='\n', indent='     '):
    with open(filename, 'w') as output_file:
        output_file.write('[')
        for count_output_file_lines, output_data in enumerate(csv_to_list_dict(INPUT_FILE)):
            delim = delimiter if count_output_file_lines != 0 else ""
            output_file.write(delim + newline + indent + '{')
            for count_output_data, (key, value) in enumerate(output_data.items()):
                delim = delimiter if count_output_data != 0 else ""
                output_file.write(delim + newline + f'{indent}{indent}"{key}": {value}')
            output_file.write(newline + indent + '}')
        output_file.write(newline + ']')


json_writer(OUTPUT_FILE)
