def numJewlsInStones(j: str, S: str) -> int:
    freqs = {}
    count = 0

    # 돌(S)의 빈도 수 계산
    for char in S:
        if char not in freqs:
            freqs[char] = 1

        else:
            freqs[char] += 1

    # 보석(j)의 빈도 수 합산
    for char in j:
        if char in freqs:
            count += freqs[char]

    return count


jew = "aA"
stone = "aAAbbbb"
jcount = numJewlsInStones(jew, stone)

print(jcount)
