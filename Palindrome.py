def isPalindrome(s: str) -> bool:
    strs = []
    self.s = s
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True



test_case: str = "A man, a plan, a canal: Panama"

result: bool = isPalindrome(test_case)
print(result) # 결과 : True


