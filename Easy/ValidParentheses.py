def isValid(s: str) -> bool:
    stack = []
    pair_dict = {"[": "]", "{": "}", "(": ")"}
    for index, char in enumerate(s):
        if len(stack) == 0 and char not in pair_dict.keys():
            return False
        elif char in pair_dict.keys():
            stack.append(char)
        elif len(stack) > 0:
            if char == pair_dict[stack[-1]]:
                stack.pop()
            else:
                return False
    return stack == []


def solution_one(s: str):
    """
    Using Stack & Hashmap. More optimized than sol2.

    :param s: String, string containing parentheses characters
    :return: Boolean
    """
    stack = [0]
    mapping = {0: None, '(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in mapping:
            stack.append(c)
        else:
            if mapping[stack.pop()] != c: return False
    return stack == [0]


def solution_two(s: str):
    """
    Using Stack & Dictionary. Great but not the best.

    :param s: String, string containing parentheses characters
    :return: Boolean
    """
    stack = []
    parentth_dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in parentth_dict.values():
            stack.append(char)
        elif char in parentth_dict.keys():
            if stack == [] or parentth_dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []


if __name__ == '__main__':
    # CASE 1: ']'
    # CASE 2: '(]'
    # CASE 3: '[)]'

    test = '(])'
    result = isValid(test)
    print(result)
