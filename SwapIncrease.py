class Solution:
    def possible(self, nums):
        ordered = list(nums)
        ordered.sort()
        for i in range(len(ordered) - 1):
            if ordered[i] == ordered[i + 1]:
                return False
        if ordered == nums:
            return True
        while ordered[0] == 0:
            ordered.remove(0)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums.copy()
                temp[i], temp[j] = temp[j], temp[i]
                while temp[0] == 0:
                    temp.remove(0)
                if temp == ordered:
                    return True
        return False


so = Solution()
inArr = [13, 31, 30]
print(so.possible(inArr))
