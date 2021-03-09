import collections


def newJewelsInStones(J: str, S: str) -> int:
    freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
    count = 0

    # 비교 없이 보석(j) 빈도 수 계산
    for char in J:
        count += freqs[char]

    return count


jew = "aA"
stone = "aAAbbbb"
jcount = newJewelsInStones(jew, stone)

print(jcount)