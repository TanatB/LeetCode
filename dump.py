def mergeAlternately(word1: str, word2: str) -> str:
    base_str = min(word1, word2)
    ans = []
    
    for i,v in enumerate(base_str):
        ans.append(word1[i])
        ans.append(word2[i])
        
    if base_str == word1:
        ans.append(word2[len(base_str):])
    else:
        ans.append(word1[len(base_str):])
    
    return "".join(ans)

# Have 2 pointers method
def mergeAlternately2(word1: str, word2: str) -> str:
    pass


if __name__ == '__main__':
    a = "abcd"
    b = 'pq'
    
    print(mergeAlternately(a, b))