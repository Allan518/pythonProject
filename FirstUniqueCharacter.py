from collections import defaultdict


class Solution:
    def first_unique_character(self, arr: str) -> int:
        hash = defaultdict(int)
        for i in range(len(arr)):
            if hash[arr[i]] == 0:
                hash[arr[i]] = i + 1
            elif hash[arr[i]] < len(arr) + 1:
                hash[arr[i]] = len(arr) + 1
        return min(hash.values()) if min(hash.values()) < len(arr) + 1 else -1


so = Solution()
arr = "abcdccacb"
print(so.first_unique_character(arr))
