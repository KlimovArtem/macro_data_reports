import argparse
import csv
import logging
import logging.config
from pathlib import Path
import os

from dotenv import load_dotenv
import yaml

from converters import DataObjectFromCSV
from formaters import TabulateReportFormater
from reports import AverageGDPReportFabric


load_dotenv()

with open(os.getenv("LOG_CONFIG_FILE", "log-config.yaml"), "r") as file:
    config = yaml.safe_load(file)
    logging.config.dictConfig(config)

logger = logging.getLogger("main")

parser = argparse.ArgumentParser(
    description="""
    Скрипт предназначен для анализ переданных макроэкономических данных в формате csv
    и печать отчетов в консоль
    """
)
parser.add_argument(
    "-f", "--files", nargs="+", type=str, help="Пути к файлам с данными для анализа, разделенные пробелом"
)
parser.add_argument("-r", "--report", type=str, help="Тип отчета который нужно сформировать")


def average_gdp(csv_files: list[str]):
    converter = DataObjectFromCSV(reader=csv.DictReader)
    formater = TabulateReportFormater()
    data = []
    for csv_file in csv_files:
        if Path(csv_file).exists():
            data += converter.converte_data(csv_file)
        else:
            raise FileNotFoundError(f"Файл {csv_file} не найден, проверьте расположение файла.")
    report = AverageGDPReportFabric(data, formater=formater)
    report.print_report()


if __name__ == "__main__":
    args = parser.parse_args()
    files = args.files
    func_name = args.report.replace("-", "_")
    func = globals().get(func_name)
    func(files)
