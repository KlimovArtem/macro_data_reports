import csv
from pathlib import Path

import pytest

from macrodata_reports.data_objects import DataObject
from macrodata_reports.converters import BaseFromCSVConverter, DataObjectFromCSV
from macrodata_reports.reports import BaseReportFabric, AverageGDPReportFabric
from macrodata_reports.formaters import BaseReportFormater, TabulateReportFormater
from macrodata_reports.main import average_gdp


def test_data_object_validation():
    # Test integer validation
    obj = DataObject(val="123")
    assert obj.val == 123

    # Test float validation
    obj = DataObject(val="123.45")
    assert obj.val == 123.45

    # Test string validation
    obj = DataObject(val="abc")
    assert obj.val == "abc"


def test_data_object_from_csv(tmp_path):
    # Create a temporary CSV file
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,value\nGDP,1000\nGrowth,2.5", encoding="utf-8")

    converter = DataObjectFromCSV(reader=csv.DictReader)
    data = converter.converte_data(str(csv_file))

    assert len(data) == 2
    assert data[0].name == "GDP"
    assert data[0].value == 1000
    assert data[1].name == "Growth"
    assert data[1].value == 2.5


def test_average_gdp_function(tmp_path):
    # Create temp CSV files
    f1 = tmp_path / "econ1.csv"
    f1.write_text("country,gdp\nUSA,21.43\nChina,14.34", encoding="utf-8")
    f2 = tmp_path / "econ2.csv"
    f2.write_text("country,gdp\nUSA,22.00\nGermany,3.86", encoding="utf-8")
    # This should run without error and cover more lines in average_gdp
    average_gdp([str(f1), str(f2)])


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        average_gdp(["non_existent.csv"])


def test_data_object_negative_numbers():
    obj = DataObject(val="-123.45")
    assert obj.val == -123.45
    obj2 = DataObject(val="-50")
    assert obj2.val == -50


def test_base_classes():
    # Cover base class methods that do nothing
    formater = BaseReportFormater()
    formater.format({})

    fabric = BaseReportFabric([], formater=formater)
    fabric.make_report([])
    fabric.print_report()

    converter = BaseFromCSVConverter(None)
    converter.convert_data()
