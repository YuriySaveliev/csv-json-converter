import csv
import random
import math
import json
import logging

COLUMNS_COUNT = 5
ROWS_COUNT = 50

columns = list(range(COLUMNS_COUNT))
rows = list(range(ROWS_COUNT))
DATA_FILE_NAME = 'rnd.csv'
OUTPUT_FILE_NAME = 'output.json'


def create_data(rows: list, columns: list) -> list:
    return [[random.randint(1, 100) for _ in columns] for _ in rows]


def write_csv_data(file_name: str, input_data: list) -> None:
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in input_data:
            writer.writerow(row)


def create_json_data(file_name: str) -> dict:
    json_data = {}

    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            item = [int(item) for item in row]
            json_data.update({index: item})

    return json_data


def create_output_file(file_name: str, data: dict) -> None:
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting app...')

    csv_content = create_data(rows, columns)
    write_csv_data(DATA_FILE_NAME, csv_content)
    json_content = create_json_data(DATA_FILE_NAME)
    create_output_file(OUTPUT_FILE_NAME, json_content)

    logging.info('Done')


if __name__ == '__main__':
    main()
