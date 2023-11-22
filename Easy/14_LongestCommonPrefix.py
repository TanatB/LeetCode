def longestCommonPrefix(strs: list) -> str:
    """
    1 <= strs.length <= 200.
    0 <= strs[i].length <= 200.
    strs consists only lowercase letters.

    1. Find min word in strs
    2. For loop with min_word iterations
    3. Check Common Prefix

    :param strs: List of strings
    :return: String, Common Prefix
    """
    zipped = list(zip(*strs))
    common_prefix = ""
    print(zipped)
    for i in zipped:
        if len(set(i)) == 1:
            common_prefix += i[0]
        else:
            break
    return common_prefix


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    longestCommonPrefix(strs)