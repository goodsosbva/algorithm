import re

def isPalindrome(s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]', '',s)

    return s == s[::-1]

test_case: str = "A man, a plan, a canal: Panama"

result: bool = isPalindrome(test_case)
print(result) # 결과 : True