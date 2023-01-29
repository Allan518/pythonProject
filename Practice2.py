class Solution:
    def zigzag(self, numbers):
        ans = []
        for i in range(len(numbers) - 2):
            if (numbers[i] < numbers[i + 1] and numbers[i + 2] < numbers[i + 1]) or (numbers[i] > numbers[i + 1] and \
                                                                                     numbers[i + 2] > numbers[i + 1]):
                ans.append(1)
            else:
                ans.append(0)

        return ans


so = Solution()
numbers = [1, 2, 1, 3, 4]
print(so.zigzag(numbers))
