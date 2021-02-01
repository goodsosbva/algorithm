def longestPalindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            print('l:', left)
            print('r:', right)
        print('expand:', s[left + 1:right])
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        print(i)
        result = max(result,  # 값 위치 지정
                     expand(i, i + 1),  # 2 칸짜리
                     expand(i, i + 2),  # 3 칸짜리
                     key=len)

    #print('result', result)
    return result


string = 'ababad'
a = longestPalindrome(string)
print(a)
