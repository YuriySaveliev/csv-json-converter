import csv
import random
import math
import json

columns_number = 5
rows_number = 50

columns = range(columns_number)
rows = range(rows_number)
row_content = []
json_data = []
data_file_name = 'rnd.csv'
output_file_name = 'output.json'

def create_data(row_number, column_number):
    csv_content = []
    for row in row_number:
        row_content = []
        for column in column_number:
            row_content.append(math.ceil(random.random() * 100))
        csv_content.append(row_content)

    return csv_content

def write_csv_data(file_name, input_data):
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in input_data:
            writer.writerow(row)

def create_json_data(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            for column in row:
                json_data.append(json.dumps({index: column}))

    return json_data

def create_output_file(file_name, data):
    with open(file_name, 'w') as jsonfile:
        writer = csv.writer(jsonfile)
        for row in data:
            writer.writerow(row)

def init():
    csv_content = create_data(rows, columns)
    write_csv_data(data_file_name, csv_content)
    json_content = create_json_data(data_file_name)
    create_output_file(output_file_name, json_content)

init()