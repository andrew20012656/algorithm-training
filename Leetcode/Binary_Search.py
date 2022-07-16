### Leetcode Problem 704 Binary Search

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low, high = 0, len(nums) - 1
    while(low <= high):
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
    return -1