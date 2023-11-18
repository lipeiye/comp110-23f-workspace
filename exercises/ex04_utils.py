"""EX03- Structured Wordle."""
__author__ = "730698337"


def all(check_list: list[int], check_num: int) -> bool:
    """This fuction check the whether all of the number in the list is indentical with the input number."""
    check_index: int = 0
    whether_all: bool = True
    if (len(check_list) == 0):
        whether_all = False
        return whether_all
    while (check_index < len(check_list)):
        if (check_num != check_list[check_index]):
            whether_all = False
        check_index += 1
    return whether_all


def max(input: list[int]) -> int:
    """This function check the max number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        max_index: int = 1
        max_num: int = input[0]
        while (max_index < len(input)):
            if (max_num < input[max_index]):
                max_num = input[max_index]
            max_index += 1
        return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """This function check whether all the number in one list is equal the numbers in the other list."""
    equal_result: bool = False
    equal_index: int = 0
    if (len(list_1) != len(list_2)):
        return equal_result
    else:
        if (len(list_1) == 0):
            return True
        while (equal_index < len(list_1)):
            if (list_1[equal_index] != list_2[equal_index]):
                equal_result = False
                return equal_result
            else:
                equal_result = True
            equal_index += 1
        return equal_result