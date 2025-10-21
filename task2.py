import re
from typing import Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"\d+\.?\d*"
    numbers_as_strings = re.findall(pattern, text) #list of numbers
    for number_str in numbers_as_strings:
        yield float(number_str)

def sum_profit(text: str, func: Callable):
    return sum(func(text))