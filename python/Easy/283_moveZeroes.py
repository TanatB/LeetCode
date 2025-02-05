def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left_pointer = 0
    for right_pointer, value in enumerate(nums):
        if value == 0:
            continue
        else:
            nums[right_pointer], nums[left_pointer] = nums[left_pointer], nums[right_pointer]
            left_pointer += 1


if __name__ == '__main__':
    nums1 = [0, 5, 0, 3, 12]
    moveZeroes(nums1)

    print(nums1)
