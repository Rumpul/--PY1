import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', newline='\n') -> list[dict]:
    with open(filename) as input_file:
        json_data = []
        headings = input_file.readline().rstrip().split(delimiter)
        for line in input_file:
            input_line = line.strip().split(newline)
            for current_line in input_line:
                json_data.append(dict(zip(headings, current_line.split(delimiter))))

        return json_data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
