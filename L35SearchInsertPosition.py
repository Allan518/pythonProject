class Solution:
    def search_insert(nums, target):
        low = 0
        high = len(nums) - 1
        if target > nums[high]:
            return high + 1
        while low != high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        return high

    print(search_insert([1, 3, 5, 6], 7))
