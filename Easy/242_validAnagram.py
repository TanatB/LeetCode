""" My Solution"""
from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    s_freq, t_freq = {}, {}

    if len(s) != len(t):
        return False

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    return s_freq == t_freq


""" More Optimal Solution"""
def isAnagram2(s: str, t: str) -> bool:
    check_dict = defaultdict(int)

    for char in s:
        check_dict[char] += 1

    for char in t:
        check_dict[char] -= 1

    for value in check_dict.values():
        if value != 0:
            return False

    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    s2 = "rat"
    t2 = "car"

    print(isAnagram2(s2, t2))