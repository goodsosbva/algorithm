def numJewelsInStones(J: str, S: str) -> int:
    return sum(s in J for s in S)


jew = "aA"
stone = "aAAbbbbaa"
jcount = numJewelsInStones(jew, stone)

print(jcount)