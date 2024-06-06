import pytest
from python.atividades.atividade11_custom_sort import custom_sort

def test_custom_sort():
    numbers = [5, 2, 8, 1, 9]
    expected_result = [9, 8, 5, 2, 1]
    assert custom_sort(numbers) == expected_result

    numbers = [3, 6, 1, 9, 4]
    expected_result = [9, 6, 4, 3, 1]
    assert custom_sort(numbers) == expected_result

    numbers = [10, 5, 2, 7, 3]
    expected_result = [10, 7, 5, 3, 2]
    assert custom_sort(numbers) == expected_result


if __name__ == "__main__":
    pytest.main()