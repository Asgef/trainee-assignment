import pytest
from .test_fetch_data import read_fixture_file
from matrix_crawler.matrix_parsing import prepare_matrix

from matrix_crawler.exceptions import (
    MatrixFormatError, MatrixNotSquareError
)


data_case_1 = read_fixture_file('required_matrix.txt')
data_case_2 = (
        '+---+\n'
        '|404|\n'
        '+---+\n'
    )

expected_case_1 = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]
    ]
expected_case_2 = [[404]]


test_cases = [
    (prepare_matrix, data_case_1, expected_case_1),
    (prepare_matrix, data_case_2, expected_case_2),
]


@pytest.mark.parametrize('prepare_matrix_func, data, expected', test_cases)
def test_prepare_matrix_success(prepare_matrix_func, data, expected):
    assert prepare_matrix_func(data) == expected


test_case_1 = read_fixture_file('non_square_matrix_1.txt')
test_case_2 = read_fixture_file('non_square_matrix_2.txt')
test_case_3 = (
        '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
        '<title>Title</title></head><body></body></html>'
    )
test_case_4 = ''
test_case_5 = 'I404I\n'


expected_case_1 = MatrixNotSquareError
expected_case_2 = MatrixNotSquareError
expected_case_3 = MatrixFormatError
expected_case_4 = MatrixFormatError
expected_case_5 = MatrixFormatError


test_cases = [
    (prepare_matrix, test_case_1, expected_case_1),
    (prepare_matrix, test_case_2, expected_case_2),
    (prepare_matrix, test_case_3, expected_case_3),
    (prepare_matrix, test_case_4, expected_case_4),
    (prepare_matrix, test_case_5, expected_case_5),
]


@pytest.mark.parametrize('prepare_matrix_func, data, expected', test_cases)
def test_prepare_matrix_unsuccessful(prepare_matrix_func, data, expected):
    with pytest.raises(expected):
        prepare_matrix(data)
