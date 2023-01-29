from collections import defaultdict
from typing import List


class Solution:
    def whole_minute_dilemma(self, arr: List[int], n: int) -> int:
        hash = defaultdict(int)
        res = 0
        for num in arr:
            if hash[(60 - num % 60) % 60] > 0:
                res += hash[(60 - num % 60) % 60]
            hash[num % 60] += 1
        return res


so = Solution()
n = 6
arr = [3, 60, 60, 60]
print(so.whole_minute_dilemma(arr, n))
