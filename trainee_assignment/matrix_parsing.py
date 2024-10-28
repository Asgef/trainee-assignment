import re
from .exceptions import MatrixFormatError, MatrixNotSquareError
from .matrix_operation import matrix_is_square


def contain_digit(data: str) -> bool:
    return bool(re.search(r'\d', data))


def contain_letter(data: str) -> bool:
    return bool(re.search(r'[a-zA-Z]', data))


def parse_matrix(lines: list[str]) -> list[list[int]]:
    return [
        [int(elem.strip()) for elem in line.split('|') if elem.strip()]
        for line in lines if contain_digit(line)
    ]


def prepare_matrix(data: str) -> list[list[int]]:
    if ('\n' not in data or '|' not in data) or not data:
        raise MatrixFormatError('Invalid matrix format')

    lines = data.split('\n')
    for line in lines:
        if contain_letter(line):
            raise MatrixFormatError('Matrix contains letters')

    matrix = parse_matrix(lines)

    if not matrix_is_square(matrix):
        raise MatrixNotSquareError('Matrix is not square')
    return matrix
