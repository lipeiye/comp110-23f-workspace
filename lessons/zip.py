
"""Combining two lists into a dictionary."""
__author__ = "730698337"


def zip(key_list: list[str], value_list: list[int]) -> dict[str, int]: 
    """Combining two list into a dictionary list."""
    output: dict[str, int] = {}
    if (len(key_list) != len(value_list) or len(key_list) == 0 or len(value_list) == 0):
        return output
    else:
        idx: int = 0
        while (idx < len(key_list)):
            output[key_list[idx]] = value_list[idx]
            idx += 1
        return output