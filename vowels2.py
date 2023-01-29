from typing import List


class Solution:
    def vowels(self, arr, queries):
        prefixSums = [0]
        total, res = 0, []
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i in range(len(arr)):
            if arr[i][0] in vowels and arr[i][-1] in vowels:
                total += 1
            prefixSums.append(total)
        for i in range(len(queries)):
            pos = queries[i].split("-")
            res.append(prefixSums[int(pos[1])] - prefixSums[int(pos[0]) - 1])
        return res

strArr = ['aba', 'bcb', 'ece', 'aa', 'ef']

strArr1 = ['abc', 'aba', 'aaa', '0', 'e']
queries = ["2-5", "1-3", "1-5"]
so = Solution()
print(so.vowels(strArr1, queries))
