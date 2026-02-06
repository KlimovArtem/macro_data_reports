from data_objects import DataObject


class BaseFromCSVConverter:
    """
    Converte csv data to other format.

    reader: is a class or function used to read data from csv files
    """

    def __init__(self, reader):
        self.reader = reader

    def convert_data(self):
        pass


class DataObjectFromCSV(BaseFromCSVConverter):
    def converte_data(self, csv_file: str) -> list[DataObject]:
        with open(csv_file, "r", encoding="utf-8") as file:
            data_sheet = [DataObject(**row) for row in self.reader(file)]
            return data_sheet
