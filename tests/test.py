import pytest
import sys
sys.path.append('C:/Users/MYaO/PycharmProjects/Testing_ivpko')
from src.library import fibonachi
from src.library import bubble_sort
from src.library import calculator

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [1, 1]),
    (0, []),
])

def test_fibonachi(n, expected):
    assert fibonachi(n) == expected

@pytest.mark.parametrize("arr,expected", [
    ([], []),
    ([5], [5]),
    (["a", "c", "b"], ["a", "b", "c"]),
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
    ("hel", "lo", "+", "hello"),
])

def test_calculator(number1, number2, operation, expected):
    assert calculator(number1, number2, operation) == expected
