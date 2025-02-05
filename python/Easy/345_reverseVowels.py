def reverseVowels(s: str) -> str:
    left, right = 0, len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s) # why
    
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return ''.join(s)

if __name__ == '__main__':
    input = "IceCreAm"
    print(reverseVowels(input))