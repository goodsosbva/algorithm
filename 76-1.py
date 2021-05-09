import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        print(need)
        missing = len(t)
        left = start = end = 0

        print(list(enumerate(s, 1)))

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    # print(need)
                    need[s[left]] += 1
                    left += 1
                    # print(need)

                if not end or right - left <= end - start:  # 출력 담당 (처음 이거나 또는 범위 밖을 넘어가지 않을 때)
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
            # print(s[start:end])
        return s[start:end]


sol = Solution()
chk = sol.minWindow("AD0BEC0DEBANC", "ABC")
print(chk)
