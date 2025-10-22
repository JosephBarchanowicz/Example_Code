import csv
import json

class CsvToJson:
    def __init__(self, file):
        self.file = file
        to_dict = self._csv_to_dict(file)
        self._dict_to_json(to_dict)


    def _csv_to_dict(self, file):
        with open('example_csv.csv', mode='r', newline='') as file:
            data = list(csv.DictReader(file))
            return data


    def _dict_to_json(self, data):
        with open('output.json', mode='w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    c = CsvToJson("example_csv.csv")