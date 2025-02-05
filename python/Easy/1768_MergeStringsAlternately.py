""" My Solution"""
def mergeAlternately(word1: str, word2: str) -> str:
    ans = ""
    if len(word1) > len(word2):
        shortLength = len(word2)
        longWord = word1
    else:
        shortLength = len(word1)
        longWord = word2


    diff = abs(len(word1) - len(word2))

    for index in range(shortLength):
        ans += word1[index]
        ans += word2[index]

    for i in range(shortLength, shortLength + diff):
        ans += longWord[i]

    return ans

""" Optimal Solution"""
def mergeAlternately2(word1: str, word2: str) -> str:
    ans = ""
    remainder_char = ""
    len1 = len(word1)
    len2 = len(word2)

    if len1 > len2:
        remainder_char = word1[len2:]
    else:
        remainder_char = word2[len1:]

    for index in range(min(len1, len2)):
        ans += word1[index]
        ans += word2[index]

    ans += remainder_char
    return ans

if __name__ == '__main__':
    word1, word2 = "abcd", "pq"
    combine1 = mergeAlternately2(word1, word2)
    print(combine1)
