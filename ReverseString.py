from typing import List

class revrse:
    def revrseStirng(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def revrseStirngPythpn(self, s: List[str]) -> None:
        s.reverse()

a = revrse()
#InputString = str(input())
InputString = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

#print(InputString)
#print(a.revrseStirng(InputString))
a.revrseStirng(InputString)
print(InputString)
a.revrseStirngPythpn(InputString)
print(InputString)


