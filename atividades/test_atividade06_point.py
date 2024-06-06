import pytest
from python.atividades.atividade06_point import Point

def test_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    expected_distance = 5

    actual_distance = p1.distance_to(p2)

    assert actual_distance == expected_distance

def test_distance_to_with_invalid_argument():
    p = Point(0, 0)

    with pytest.raises(ValueError):
        p.distance_to("invalid")

pytest.main()