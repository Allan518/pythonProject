from typing import List


class Solution:
    def collect_below_threshold(nums: List[int], threshold: int) -> List[int]:
        below_threshold = []
        for num in nums:
            if num < threshold:
                below_threshold.append(num)
        return below_threshold

    def scale_midterm_grades(grades: List[int], multiplier: int, bonus: int) -> None:
        for n in range(len(grades)):
            grades[n] = min(grades[n] * multiplier + bonus, 100)

    def count_odds(values: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(values)):
            count = 0
            for j in range(len(values[i])):
                if values[i][j] % 2 == 1:
                    count += 1
            result.append(count)
        return result
    values = [[1, 2], [8], [5, 6, 7]]
    print(count_odds(values))
