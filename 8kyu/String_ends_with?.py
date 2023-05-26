"""
String ends with?(https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python)

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""
from ast import literal_eval


def solution(text, ending):
    if text[::-1].find(ending[::-1]) == 0:
        return True
    else:
        return False
