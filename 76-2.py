
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        current_count = collections.Counter()
        print(current_count)

        start = float('-inf')
        end = float('inf')

        left = 0
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            current_count[char] += 1
            print(current_count)

            # AND 연산 결과로 왼쪽 포인터 이동 판단
            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1

        return s[start: end] if end - start <= len(s) else ''


sol = Solution()
chk = sol.minWindow("AD0BEC0DEBANC", "ABC")
print(chk)