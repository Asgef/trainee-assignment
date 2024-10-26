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


def matrix_is_square(data: list[list[int]]) -> bool:
    if not data:
        return False
    return len(data) == len(data[0])


def matrix_to_spiral(data: list[list[int]]) -> list[int]:  # noqa C901
    if not data or not matrix_is_square(data):
        return []
    if len(data) == 1:
        return data[0]

    result = []
    top, bottom = 0, len(data) - 1
    left, right = 0, len(data[0]) - 1

    while left <= right and top <= bottom:
        # Шагаем в низ по левой границе
        for i in range(top, bottom + 1):
            result.append(data[i][left])
        left += 1

        # Шагаем вправо по нижней границе
        for i in range(left, right + 1):
            result.append(data[bottom][i])
        bottom -= 1

        # Шагаем вверх по правой границе
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(data[i][right])
            right -= 1

        # Шагаем влево по верхней границе
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(data[top][i])
            top += 1

    return result
