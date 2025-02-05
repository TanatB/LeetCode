def repeatedSubstringPattern(s: str) -> bool:
    # Needs to be reviewed again (I don't really get the optimal answer).
    s_len = len(s)
    for i in range(1, int(s_len / 2) + 1):
        if s_len % i == 0:
            num_repeats = int(s_len / i)
            s_sub = s[0:i]
            sub_string = ""
            for j in range(num_repeats):
                sub_string += s_sub
            if sub_string == s:
                return True

    return False


if __name__ == '__main__':
    s = "abab"

    print(repeatedSubstringPattern(s))