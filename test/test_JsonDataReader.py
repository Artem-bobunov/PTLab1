import pytest
from typing import Tuple
from Types import DataType
from JsonDataReader import JsondataReader


class TestJsonDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> Tuple[str, DataType]:
        text = '{ "Иванов Константин Дмитриевич": {\n' + \
            ' "математика": 91, \n' + ' "химия": 100 },\n' + \
            ' "Петров Петр Семенович": {\n' + \
            ' "русский язык": 87,\n' + ' "литература": 78 } }'

        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content:
                          Tuple[str, DataType],
                          tmpdir) -> Tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: Tuple[str, DataType]) -> None:
        file_content = JsondataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
