import csv
import random
import math
import json

COLUMNS_COUNT = 5
ROWS_COUNT = 50

columns = range(COLUMNS_COUNT)
rows = range(ROWS_COUNT)
DATA_FILE_NAME = 'rnd.csv'
OUTPUT_FILE_NAME = 'output.json'


def create_data(row_number, column_number):
    return [[math.ceil(random.random() * 100) for column in column_number] for row in row_number]


def write_csv_data(file_name, input_data):
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in input_data:
            writer.writerow(row)


def create_json_data(file_name):
    json_data = {}

    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            new_list = [int(item) for item in row]
            json_data.update(dict({index: new_list}))

    return json_data


def create_output_file(file_name, data):
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)


def init():
    csv_content = create_data(rows, columns)
    write_csv_data(DATA_FILE_NAME, csv_content)
    json_content = create_json_data(DATA_FILE_NAME)
    create_output_file(OUTPUT_FILE_NAME, json_content)


init()
