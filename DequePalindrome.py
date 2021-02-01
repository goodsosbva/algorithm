import collections
from collections import deque
from typing import Deque
import collections


def isPalindrome(s: str) -> bool:

    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

test_case: str = "A man, a plan, a canal: Panama"

result: bool = isPalindrome(test_case)
print(result) # 결과 : True