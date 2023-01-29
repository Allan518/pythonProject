from typing import List


class Solution:
    def max_pos_prefixes(self, arr: List[int], n: int) -> int:
        arr.sort(reverse=True)
        sum, ans = 0, 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum <= 0:
                return i
            ans += 1
        return ans

so = Solution()
arr = [1, 2, 3, -9, 0, -8]
print(so.max_pos_prefixes(arr, 5))

