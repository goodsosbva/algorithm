# 파이썬 방식
class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)


matrix = \
    [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
sol = Solution()
check = sol.searchMatrix(matrix, 5)
print(check)