"""Test my zip function."""
__author__ = "730698337"
from lessons.zip import zip
"""Import the zip function from zip."""


def test_zip_usecase_1() -> None:
    """This function test the first usecase."""
    key_list: list[str] = ["li", "peiye"]
    value_list: list[int] = [2, 1]
    assert zip(key_list, value_list) == {"li": 2, "peiye": 1}


def test_zip_usecase_2() -> None:
    """This function test the second usecase."""
    key_list2: list[str] = ["chocolate", "apple"]
    value_list2: list[int] = [12, 13]
    assert zip(key_list2, value_list2) == {"chocolate": 12, "apple": 13}


def test_zip_usecase_3() -> None:
    """This function test the edge case."""
    key_list3: list[str] = ["Peiye"]
    value_list3: list[int] = [1, 2, 3]
    assert zip(key_list3, value_list3) == {"Peiye": 1}