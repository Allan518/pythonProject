from typing import List
from collections import defaultdict


class Solution:
    def closest_numbers(self, arr: List[int], n: int):
        arr.sort()
        min = float("inf")
        res = defaultdict(list)
        for fv, sv in zip(arr, arr[1:]):
            if sv - fv <= min:
                min = sv - fv
                res[min].append((fv, sv))
        for fv, sv in res[min]:
            print(str(fv) + " " + str(sv))


so = Solution()
arr = [2, 5, 9, -4, -2, 0]
n = 7
so.closest_numbers(arr, n)
