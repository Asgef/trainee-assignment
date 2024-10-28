Hi, this mini project is my practice and implementation of . [this test assignment](https://github.com/avito-tech/python-trainee-assignment).

[![Maintainability](https://api.codeclimate.com/v1/badges/87bd256fc9bedd2b48cb/maintainability)](https://codeclimate.com/github/Asgef/trainee-assignment/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/87bd256fc9bedd2b48cb/test_coverage)](https://codeclimate.com/github/Asgef/trainee-assignment/test_coverage)


# Matrix Crawler

`matrix_crawler` is a Python library designed to retrieve, validate, and convert matrix data from a remote server, outputting elements in a counterclockwise spiral traversal order. The library supports asynchronous HTTP requests and performs data validation for consistent matrix operations.

## Installation

You can install the library directly from GitHub using Poetry:

```bash
poetry add git+https://github.com/your_username/matrix_crawler.git
```

Or with pip:

```bash
pip install git+https://github.com/your_username/matrix_crawler.git
```

## Usage Example
The following example demonstrates how to use get_matrix to fetch and process a matrix from a given URL, traversing it in a counterclockwise spiral order:


```python
from matrix_crawler import get_matrix
import asyncio

SOURCE_URL = (
    'https://raw.githubusercontent.com/avito-tech/'
    'python-trainee-assignment/main/matrix.txt'
)

# Expected traversal order output (counterclockwise)
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

# Retrieve and print the matrix in spiral order
print(asyncio.run(get_matrix(SOURCE_URL)))
```

This example retrieves a matrix from the specified 'SOURCE_URL' and outputs its elements in a counterclockwise spiral order traversal.
