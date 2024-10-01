#!/usr/bin/python3
"""
this module contains functions to convert csv to json
"""
import json
import csv


def convert_csv_to_json(csv_file):
    data = []

    try:
        with open(csv_file, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)

            for rows in csvReader:
                data.append(rows)

    except FileNotFoundError:
        print("file not found")
        return False
    json_data = json.dumps(data)
    try:
        with open("data.json", 'w', encoding="utf-8") as f:
            f.write(json_data)
        return True

    except FileNotFoundError:
        print("file not found")
    return False
