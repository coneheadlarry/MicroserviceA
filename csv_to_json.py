import os
import csv
import json
import time


class CSVToJSONMicroservice:
    def __init__(self, interval=5):
        self.base_directory = os.path.dirname(os.path.abspath(__file__))
        self.csv_directory = os.path.join(self.base_directory, 'CSVs')
        self.interval = interval
        self.request_file = os.path.join(self.base_directory, 'bulkimport.txt')

    def start(self):
        while True:
            if os.path.exists(self.request_file):
                with open(self.request_file, 'r') as file:
                    csv_filename = file.read().strip() + '.csv'
                if self.csv_exists(csv_filename):
                    self.csv_to_json(csv_filename)
                else:
                    print(f"File '{csv_filename}' not found")
            time.sleep(self.interval)

    def csv_exists(self, csv_filename):
        return os.path.exists(os.path.join(self.csv_directory, csv_filename))

    def csv_to_json(self, csv_filename):
        csv_data = self.read_csv(csv_filename)
        json_data = self.convert_to_json(csv_data)
        self.save_json(json_data, 'output.json')
        os.remove(self.request_file)

    def read_csv(self, csv_filename):
        with open(os.path.join(self.csv_directory, csv_filename), 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return [row for row in csv_reader]

    def convert_to_json(self, csv_data):
        return json.dumps(csv_data, indent=4)

    def save_json(self, json_data, json_filename):
        with open(os.path.join(self.base_directory, json_filename), 'w') as json_file:
            json_file.write(json_data)


if __name__ == "__main__":
    service = CSVToJSONMicroservice()
    service.start()
