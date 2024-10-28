import pytest
from trainee_assignment.exceptions import (
    MatrixFormatError, MatrixNotSquareError
)
from .test_fetch_data import read_fixture_file
from trainee_assignment.matrix_utils import prepare_matrix


def test_convert_str_to_matrix_success_1():
    str_data = read_fixture_file('required_matrix.txt')
    data = prepare_matrix(str_data)
    assert data == [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]
    ]

def test_convert_str_to_matrix_success_2():
    str_data = (
        '+---+\n'
        '|404|\n'
        '+---+\n'
    )
    data = prepare_matrix(str_data)
    assert data == [
        [404]
    ]


def test_convert_str_to_matrix_unsuccessful_1():
    with pytest.raises(MatrixFormatError):
        prepare_matrix(
        '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
        '<title>Title</title></head><body></body></html>'
    )


def test_convert_str_to_matrix_unsuccessful_2():
    with pytest.raises(MatrixFormatError):
        prepare_matrix('')


def test_convert_str_to_matrix_unsuccessful_3():
    with pytest.raises(MatrixFormatError):
        prepare_matrix('I404I\n')


def test_convert_str_to_matrix_unsuccessful_4():
    with pytest.raises(MatrixFormatError):
        prepare_matrix('<404>\n')

def test_convert_str_to_matrix_unsuccessful_5():
    with pytest.raises(MatrixNotSquareError):
        prepare_matrix(read_fixture_file('non_square_matrix.txt'))
