import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        # print(s)
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # print(counts)
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]
            # print(right, left)

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left


S = "AAABBC"
k = 2
sol = Solution()
chk = sol.characterReplacement(S, k)
print(chk)
