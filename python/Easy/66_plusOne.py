def plusOne(digits: list[int]) -> list[int]:
    total = ""
    for digit in digits:
        total += str(digit)

    plus_one = int(total) + 1

    ans = []
    for i in str(plus_one):
        ans.append(int(i))

    return ans


if __name__ == '__main__':
    digits1 = [9]
    print(plusOne(digits1))
