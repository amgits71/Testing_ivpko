import pytest
import sys
sys.path.append('C:/Users/MYaO/PycharmProjects/Testing_ivpko')
from src.library import fibonachi
from src.library import bubble_sort
from src.library import calculator

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [1, 1]),
    (-1, "I"),
    (0, []),
    (2.5, [1, 1, ]),
    ("2.5", 0),
])

def test_fibonachi(n, expected):
    assert fibonachi(n) == expected

@pytest.mark.parametrize("arr,expected", [
    ([], []),
    ([5], [5]),
    (["a", "c", "b"], ["a", "b", "c"]),
    (-1, []),
    ([3, 1, 4, 2], [1, 2, 3, 4]),
    ([2, 2, 2],  [2, 2, 2]),
])

def test_bubble_sort(arr, expected):
    assert bubble_sort(arr) == expected

@pytest.mark.parametrize("number1, number2, operation,expected", [
    (5, 3, "+", 8),
    (10, 4, "-", 6),
    (4, 7, "*", 28),
    (15, 5, "/", 3),
    (10, 0, "/", 0),
    (5, 2, "%", 1),
    ("hel", "lo", "+", "hello"),
    ("abc", 7, "-", [])
])

def test_calculator(number1, number2, operation, expected):
    assert calculator(number1, number2, operation) == expected
