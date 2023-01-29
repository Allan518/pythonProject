class Solution:
    def removeDuplicates(nums):
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != curr:
                curr = nums[i]
            else:
                nums.pop(i)
                i -= 1

    removeDuplicates([1, 1, 2])
