class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


sol = Solution()
chk = sol.hammingDistance(1, 4)
print(chk)