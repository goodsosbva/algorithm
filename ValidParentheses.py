def ivValid(s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }