"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order
  they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.

Constraints:

1. 1 <= nums.length <= 3 * 104
2. -100 <= nums[i] <= 100
3. nums is sorted in non-decreasing order.

If all assertions pass, then your solution will be accepted.

Last edited: 09-Sep-2023
Problem Status: Accepted
Runtime: 85ms (Beats 70.69%)
Memory: 17.99MB (Beats 50.5%)
"""


def removeDuplicates(nums: list[int]) -> int:
    explored, first_appear = set(), list()
    count = 0
    for index, value in enumerate(nums):
        if value not in explored:
            explored.add(value)
            first_appear.append(index)
            count += 1
        continue

    for i in range(count):
        nums[i], nums[first_appear[i]] = nums[first_appear[i]], nums[i]

    return count


if __name__ == '__main__':
    numbers = [0, 0, 1, 1, 1, 1, 2, 2, 2, 4]  # Input array
    # first_appear = [0,2,6,9]
    # explored = {0,1,2,4}
    print(removeDuplicates(numbers))    # Should print 4
    print(numbers)
    expectedNums = [0, 1, 2, 4, 1, 1, 0, 2, 2, 1]  # The expected answer with correct length
