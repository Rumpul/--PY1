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
    line_count = sum(1 for line in open(INPUT_FILE))-1
    with open(filename, 'w') as output_file:
        output_file.write('[' + newline)
        count_output_file_lines = 0
        for output_data in csv_to_list_dict(INPUT_FILE):
            output_file.write(indent + '{' + newline)
            count_output_data = 0
            for key, value in output_data.items():
                output_file.write(f'{indent}{indent}"{key}": {value}')
                if count_output_data < len(output_data)-1:
                    output_file.write(delimiter + newline)
                else:
                    output_file.write(newline)
                count_output_data += 1
            count_output_file_lines += 1
            if count_output_file_lines < line_count:
                output_file.write(indent + '}' + delimiter + newline)
            else:
                output_file.write(indent + '}' + newline)
        output_file.write(']')


json_writer(OUTPUT_FILE)
