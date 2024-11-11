def findMaxAverage(nums: list[int], k: int) -> float:
    total = sum(nums[:k])
    max_sum = total
  
    for i in range(1, len(nums) - k + 1):
        total = total - nums[i - 1] + nums[i + k - 1]
        max_sum = max(max_sum, total)
        
    return max_sum / k


if __name__ == '__main__':
    print("This is Find Max Average question.")
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(findMaxAverage(nums, k))