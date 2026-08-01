import pytest


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    return "F"

@pytest.mark.parametrize("score, expected", [
    (95, 'A'),
    (80, 'B'),
    (60, 'C'),
    (30, 'F')
])
def test_grade(score,expected):
    assert grade(score) == expected


