# Prefix Sum Question
def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    leftSum = 0
    
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    
    return -1

if __name__ == "__main__":
    nums = [2,1,-1]
    nums2 = [1,7,3,6,5,6]
    nums3 = [-1,-1,0,1,0,-1]
    print(pivotIndex(nums3))