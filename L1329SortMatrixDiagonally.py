from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp_res = []

        def dfs(i):
            if (i == len(nums)):
                res.append(tmp_res.copy())
                return
            else:
                tmp_res.append(nums[i])
                dfs(i + 1)
                tmp_res.pop()
                dfs(i + 1)

        dfs(0)
        return res


mynum = [1, 2, 3]
x = Solution()
print(x.subsets(mynum))