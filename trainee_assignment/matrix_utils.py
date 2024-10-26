import re


def contain_digit(data: str) -> bool:
    return bool(re.search(r'\d', data))


def parse_matrix(lines: list[str]) -> list[list[int]]:
    return [
        [int(elem.strip()) for elem in line.split('|') if elem.strip()]
        for line in lines if contain_digit(line)
    ]


def convert_str_to_matrix(data: str) -> list[list[int]]:
    if data == '' or '\n' not in data:
        return []

    lines = data.split('\n')
    if len(lines) < 2:
        return []

    return parse_matrix(lines)
