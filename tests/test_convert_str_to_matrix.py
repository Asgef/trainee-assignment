from .test_fetch_data import read_fixture_file
from trainee_assignment.parser import convert_str_to_matrix


def test_convert_str_to_matrix_success():
    str_data = read_fixture_file('required_matrix.txt')
    data = convert_str_to_matrix(str_data)
    assert data == [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]
    ]


def test_convert_str_to_matrix_unsuccessful_1():
    str_data = (
        '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
        '<title>Title</title></head><body></body></html>'
    )
    data = convert_str_to_matrix(str_data)
    assert data == ''


def test_convert_str_to_matrix_unsuccessful_2():
    str_data = ''
    data = convert_str_to_matrix(str_data)
    assert data == []
