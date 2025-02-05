# Two pointers
def isSubsequence(s: str, t: str) -> bool:
    one, two = 0, 0
    
    while one < len(s) and two < len(t):
        if s[one] == t[two]:
            one += 1
        two += 1
    
    if one == len(s):
        return True
    
    return False

if __name__ == "__main__":
    print("this is Subsequence question")
    s, t = "aaaaaa", "bbaaaa"
    print(isSubsequence(s, t))