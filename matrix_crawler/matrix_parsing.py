import re
from .matrix_operation import matrix_is_square
from .exceptions import MatrixFormatError, MatrixNotSquareError


def contain_digit(data: str) -> bool:
    """
    Checks if a string contains at least one digit.

    Args:
        data (str): The string to be checked.

    Returns:
        bool: True if the string contains a digit, False otherwise.
    """
    return bool(re.search(r'\d', data))


def contain_letter(data: str) -> bool:
    """
    Checks if a string contains at least one letter.

    Args:
        data (str): The string to be checked.

    Returns:
        bool: True if the string contains a letter, False otherwise.
    """
    return bool(re.search(r'[a-zA-Z]', data))


def parse_matrix(lines: list[str]) -> list[list[int]]:
    """
    Converts a list of strings into a matrix of integers.

    Each string should contain matrix elements separated by vertical bars.
    Elements should be integers.

    Args:
        lines (list[str]): A list of strings containing matrix elements.

    Returns:
        list[list[int]]: A matrix of integers.
    """
    return [
        [int(elem.strip()) for elem in line.split('|') if elem.strip()]
        for line in lines if contain_digit(line)
    ]


def prepare_matrix(data: str) -> list[list[int]]:
    """
    Prepares string data for conversion into a matrix.

    Checks that the string has the correct matrix format,
    that it does not contain letters,
    and that the resulting matrix is square.

    Args:
        data (str): String data containing a matrix.

    Returns:
        list[list[int]]: A matrix of integers.

    Raises:
        MatrixFormatError: If the string has an incorrect matrix format.
        MatrixNotSquareError: If the resulting matrix is not square.
    """
    if ('\n' not in data or '|' not in data) or not data:
        raise MatrixFormatError('Invalid matrix format')

    lines: list[str] = data.split('\n')
    for line in lines:
        if contain_letter(line):
            raise MatrixFormatError('Matrix contains letters')

    matrix: list[list[int]] = parse_matrix(lines)

    if not matrix_is_square(matrix):
        raise MatrixNotSquareError('Matrix is not square')
    return matrix
