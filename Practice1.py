class Solution:
    def code(self, a):
        b = []
        for i in range(len(a) // 2):
            if (a[i] in b) or (a[len(a) - i - 1] in b) or (a[i] == a[len(a) - i - 1]):
                return False
            b.append(a[i])
            b.append(a[len(a) - i - 1])
        if len(a) % 2 == 1:
            if a[len(a) // 2] in b:
                return False
            b.append(a[len(a) // 2])
        a.sort()
        if b == a:
            return True
        return False


so = Solution()
a = [-91, -84, -67, -44, 9, 70, 88, 37, -11, -67, -72, -87]
print(so.code(a))
