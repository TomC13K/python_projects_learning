# create test cases for the function get_names
#   test case 1: empty list
#   test case 2: list with one dictionary

from x01_01_task import get_names, sorted_names

def test_get_names_empty_list():
    assert get_names([]) == []

def test_sorted_names_empty_list():
    assert sorted_names([]) == []

