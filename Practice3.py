class Solution:
    def merge(self, s1, s2):
        d1 = {}
        d2 = {}
        ans = ""
        for i in range(len(s1)):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
        for i in range(len(s2)):
            d2[s2[i]] = d2.get(s2[i], 0) + 1
        index1, index2 = 0, 0
        while not (index1 == len(s1) - 1 and index2 == len(s2) - 1):
            if index1 == len(s1):
                for i in range(index2, len(s2)):
                    ans += s2[index2]
            if index2 == len(s2):
                for i in range(index1, len(s1)):
                    ans += s1[index1]
            if d1.get(s1[index1]) < d2.get(s2[index2]):
                ans += s1[index1]
                index1 += 1
            elif d1.get(s1[index1]) > d2.get(s2[index2]):
                ans += s2[index2]
                index2 += 1
            else:
                if s1[index1] <= s2[index2]:
                    ans += s1[index1]
                    index1 += 1
                else:
                    ans += s2[index2]
                    index2 += 1
        return ans


so = Solution()
s1 = "dce"
s2 = "cccbd"
print(so.merge(s1, s2))
