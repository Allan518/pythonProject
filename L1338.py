class Solution:
    def min_set_size(arr):
        map1 = {}
        for i in range(len(arr)):
            if map1.__contains__(arr[i]):
                map1.update({arr[i]: map1.get(arr[i]) + 1})
            else:
                map1[arr[i]] = 1
        target = len(arr) // 2 + len(arr) % 2
        sum1 = 0
        ans = 0
        for key in dict(sorted(map1.items(), key=lambda item: item[1])):
            if sum1 >= target:
                return ans
            sum1 += map1.get(key)
            ans += 1
        return ans

    print(min_set_size([9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]))
