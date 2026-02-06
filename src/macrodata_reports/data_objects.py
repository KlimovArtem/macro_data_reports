import re


class DataObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            value = DataObject.validate(value)
            setattr(self, key, value)

    @staticmethod
    def validate(value: str) -> str | int | float:
        if not isinstance(value, str):
            return value

        # Regular expression for whole and fractional numbers (including negative numbers)
        int_pattern = r"^-?\d+$"
        float_pattern = r"^-?\d+\.\d+$"

        if re.match(int_pattern, value):
            return int(value)
        elif re.match(float_pattern, value):
            return float(value)
        return value
