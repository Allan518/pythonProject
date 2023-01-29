class Solution:
    def vowels(arr, queries):
        prefixSums = [0]
        total, res = 0, []
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i in range(len(arr)):
            if arr[i][0] in vowels and arr[i][-1] in vowels:
                total += 1
            prefixSums.append(total)
        for i in range(len(queries)):
            pos = queries[i].split("-")
            res.append(prefixSums[pos[1]] - prefixSums[pos[0] - 1])
        return res

    def whole_minute_dilemma(arr):
        occurrences = {}
        ans = 0
        for i in arr:
            if 60 - i % 60 in occurrences.keys():
                ans += occurrences[60 - i % 60]
            if i % 60 in occurrences.keys():
                occurrences[i % 60] += 1
            else:
                occurrences[i % 60] = 1
        return ans

    def closest_numbers(arr, n):

        return 1



    strArr1 = ['aba', 'bcb', 'ecb', 'aa', 'e']
    queries = ["2-5", "1-3", "1-5"]
    arr = [6, 2, 4, 10]
    print(closest_numbers(arr, 4))
    print(vowels(strArr1, queries))
    str = "abcda"
    arr1 = [10, 50, 90, 30]
