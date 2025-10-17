import pytest
from functions import add_numbers, check_even, get_first_element, divic

def test_add_numbers():
    assert add_numbers([1, 2]) == 3
    assert add_numbers([0, 0]) == 0
    assert add_numbers([10, 20]) == 30
    assert add_numbers([-10, 10]) == 0

def test_check_even():
    assert check_even(2)
    assert not check_even(3)

def test_check_even_odd():
    assert check_even_odd(2) == "Even"
    assert check_even_odd(3) == "Odd"

def test_get_first_element():
    assert get_first_element([1, 2, 3]) == 1
    assert get_first_element(["a", "b"]) == "a"
    result = get_first_element([])
    assert result is None
    assert result == None

def test_get_first_element_edge_cases():
    assert get_first_element([1, 2, 3, 4]) == [1, 2]
    assert get_first_element([1]) == [1]

def test_divic_numbers():
    assert divic_numbers([0, 2]) == 0
    assert divic_numbers([9, 3]) == 3

def test_divic_numbers_precision():
    assert divic_numbers([1, 3]) == 0.34
    assert result > 0.32

def test_divic_numbers_zero_division():
    with pytest.raises(ZeroDivisionError):
        divic_numbers([5, 0])