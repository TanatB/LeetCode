""" My solution (Brute Force)"""
def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1


""" Optimal Solution (KMP)"""
def strStr1(haystack: str, needle: str) -> int:
    return -1


""" Solution (window sliding)"""
def strStr2(haystack: str, needle: str) -> int:
    return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"

    print(strStr(haystack, needle))