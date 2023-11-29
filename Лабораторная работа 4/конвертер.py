import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    a = []
    with open(INPUT_FILENAME,'r', encoding='utf-8') as z:
        file_csv = csv.DictReader(z)
        for i in file_csv:
            a.append(i)
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as n:
            json_data = json.dumps(a, indent=4, ensure_ascii=False)
            n.write(json_data)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output:
        for line in output:
            print(line, end="")