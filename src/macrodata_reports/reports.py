from data_objects import DataObject


class BaseReportFabric:
    """
    Report generator
    - formater - it's BaseReportFormater subclass;
    """

    def __init__(self, data: list[DataObject], formater=None):
        self.formater = formater
        self.report = self.make_report(data)

    def make_report(self, data):
        pass

    def print_report(self):
        pass


class AverageGDPReportFabric(BaseReportFabric):
    def make_report(self, data: list[DataObject]) -> list[dict]:
        report_mockup = {}

        for obj in data:
            if obj.country in report_mockup:
                report_mockup[obj.country].append(obj.gdp)
            else:
                report_mockup[obj.country] = [obj.gdp]
        for country, gdp_country_data in report_mockup.items():
            report_mockup[country] = sum(gdp_country_data) / len(gdp_country_data)

        return report_mockup

    def print_report(self):
        print(self.formater.format(self.report, headers=("Country", "GDP")))
