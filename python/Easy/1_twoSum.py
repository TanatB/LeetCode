"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

1. 2 <= nums.length <= 104
2. -109 <= nums[i] <= 109
3. -109 <= target <= 109
4. Only one valid answer exists.

Last edited: 09-Sep-2023
Problem Status: Accepted
Runtime:
Memory:
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    two_pair = {}
    for index, value in enumerate(nums):
        if value in two_pair:
            return [two_pair[value], index]
        else:
            two_pair[target - value] = index


if __name__ == '__main__':
    numbers = [3, 2, 4, 5]
    t = 7
    print(twoSum(numbers, t))
