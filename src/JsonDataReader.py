from Types import DataType
from DataReader import DataReader

import json

class JsondataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:

        # Open the file and load the file
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            # print(data)

            for key in data:
                self.students[key] = []
                for subject in data[key]:
                    self.students[key].append(
                    (subject, data[key][subject]))
            print(self.students)
        return self.students