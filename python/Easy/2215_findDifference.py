def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    answer = [[],[]]

    for num1 in nums1:
        if num1 not in nums2 and num1 not in answer[0]:
            answer[0].append(num1)
    
    for num2 in nums2:
        if num2 not in nums1 and num2 not in answer[1]:
            answer[1].append(num2)
            
    return answer

def opt_findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    
    ans1 = nums1 - nums2
    ans2 = nums2 - nums1
    
    return [list(ans1), list(ans2)]            


if __name__ == '__main__':
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    
    print(opt_findDifference(nums1, nums2))