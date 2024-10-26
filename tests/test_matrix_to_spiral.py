from trainee_assignment.matrix_utils import matrix_to_spiral
import pytest


data_case_1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
data_case_2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
data_case_3 = [
        [1, 2],
        [3, 4]
    ]
data_case_4 = [[1]]
data_case_5 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
data_case_6 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
data_case_7 = []

expected_case_1 = [1, 5, 9, 13, 14, 15, 16, 12, 8, 4, 3, 2, 6, 10, 11, 7]
expected_case_2 = [1, 4, 7, 8, 9, 6, 3, 2, 5]
expected_case_3 = [1, 3, 4, 2]
expected_case_4 = [1]
expected_case_5 = []
expected_case_6 = []
expected_case_7 = []


test_cases = [
    (matrix_to_spiral, data_case_1, expected_case_1),
    (matrix_to_spiral, data_case_2, expected_case_2),
    (matrix_to_spiral, data_case_3, expected_case_3),
    (matrix_to_spiral, data_case_4, expected_case_4),
    (matrix_to_spiral, data_case_5, expected_case_5),
    (matrix_to_spiral, data_case_6, expected_case_6),
    (matrix_to_spiral, data_case_7, expected_case_7)
]


@pytest.mark.parametrize("matrix_to_spiral_func, data, expected", test_cases)
def test_matrix_to_spiral(matrix_to_spiral_func, data, expected):
    assert matrix_to_spiral_func(data) == expected
