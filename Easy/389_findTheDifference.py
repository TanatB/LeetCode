import collections # Used for optimal Solution

""" My solution"""
def findTheDifference(s: str, t: str) -> str:
    for i, char in enumerate(t):
        if s.count(char) != t.count(char):
            return char


""" Optimal Solution"""
def findTheDifference2(s: str, t: str) -> str:
    countS = collections.Counter(s)
    countT = collections.Counter(t)
    for i in range(len(t)):
        if t[i] not in countS or countT[t[i]] > countS[t[i]]:
            return t[i]


if __name__ == '__main__':
    s = "aaasdffdsaasadfxbcvxbfsdfuty"
    t = "aaasdffdsaasadfxbcvxbfsdfutyw"
    print(findTheDifference(s, t))