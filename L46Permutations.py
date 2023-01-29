from typing import List


class Solution:
    res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            arr = [nums[i]]
            used = [i]
            self.recurse(arr, nums, used)
        return self.res

    def recurse(self, currArray: List[int], nums: List[int], used: List[int]):
        if len(currArray) == len(nums):
            self.res.append(currArray)
        for i in range(len(nums)):
            if i in used:
                continue
            temp = currArray.copy()
            temp.append(nums[i])
            tempUsed = used.copy()
            tempUsed.append(i)
            self.recurse(temp, nums, tempUsed)


nums = [1, 2, 3]
sol = Solution()
print(sol.permute(nums))
