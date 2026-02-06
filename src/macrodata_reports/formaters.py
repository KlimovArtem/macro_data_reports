from tabulate import tabulate


class BaseReportFormater:
    """
    Format data for represent user
    """

    def format(self, report: dict, *args, **kwargs):
        pass


class TabulateReportFormater(BaseReportFormater):
    def format(self, report: dict, headers=None, sort: bool = True, sort_reverse: bool = True):
        if sort:
            data = sorted([[key, value] for key, value in report.items()], key=lambda x: x[1], reverse=sort_reverse)
        else:
            data = [[key, value] for key, value in report.items()]
        return tabulate(data, headers=headers, showindex=True, floatfmt=".2f")
