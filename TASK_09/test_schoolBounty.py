import pytest
from schoolBounty import (
    calculate_gpa,
    normalize_scores,
    find_top_student,
    safe_divide
)

def test_calculate_gpa_normal():
    assert calculate_gpa([90, 85]) == 4.0
    assert calculate_gpa([80, 85, 82]) == 3.5
    assert calculate_gpa([70, 75, 71]) == 3.0
    assert calculate_gpa([60, 52]) == 2.0
    assert calculate_gpa([50, 40]) == 1.0
    assert calculate_gpa([30]) == 0.0

def test_calculate_gpa_boundary():
    assert calculate_gpa([100]) == 4.0
    assert calculate_gpa([0]) == 0.0

def test_normalize_scores():
    assert normalize_scores([50, 60, 70]) == [0.0, 0.5, 1.0]
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize_scores([75]) == [1.0]

def test_scholarship_eligible():
    assert assign_scholarship(4.0, 90) is True
    assert assign_scholarship(3.5, 85) is True
    assert assign_scholarship(3.0, 75) is False

def test_find_top_student():
    students = [("Alice", 95), ("Charlie", 80)]
    assert find_top_student(students) == "Bob"
    
    students = [("Alice", 90), ("Ben", 95)]
    assert find_top_student(students) == "Ben"
    
    students = [("Solo", 100)]
    assert find_top_student(students) == "Solo"

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(0, 5) == 0.0
    assert safe_divide(5, 0) is None

if __name__ == "__main__":
    pytest.main()