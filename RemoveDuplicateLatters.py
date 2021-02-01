s = 'cbacdcbc'

def Dup(s: str) -> str:
    S = set(s)
    print(S)
    S_1 = set(s)
    for char in sorted(set(s)):
        print("char: ", char)

        suffix = s[s.index(char):]
        print("Suffix: ", suffix)

        if set(s) == set(suffix):
            return char + Dup(suffix.replace(char, ''))

    return ''


Dup(s)

#print(suffix)
#print(S_1)
# import pprint

import collections


class Solution:
    def __init__(self):
        self.count = 0

    def removeDuplicateLetters(self, s: str) -> str:

        print()
        print(f'{self.count}번째 재귀함수')
        print(f's = {s}')
        self.count += 1
        tmp = 1
        for char in sorted(set(s)):
            print(f'{tmp}번째 for문 sorted(set(s)) : {sorted(set(s))}')
            tmp += 1
            suffix = s[s.index(char):]
            print(f'char = {char}')
            print(f'suffix = {suffix}')
            print(f'set(s) = {set(s)}')
            print(f'set(suffix) = {set(suffix)}')

            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))

        return ''

    def removeDuplicateLetters1(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        print(seen)
        # print(collections.Counter(s))
        # print("seen:", set("cbacdcbc"))
        for char in s:
            print(char)
            counter[char] -= 1
            print(counter, "\\\\", counter[char])
            if char in seen:
                print("if?")
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                print("while")
                print("stack", stack)
                print("stack[-1]:", stack[-1])
                seen.remove(stack.pop())
            print("append")
            stack.append(char)
            seen.add(char)
            print("seen : ", seen)
            print("stack : ", stack)

        return ''.join(stack)


answer1 = Solution().removeDuplicateLetters1("cbacdcbc")
print(f'answer : {answer1}')