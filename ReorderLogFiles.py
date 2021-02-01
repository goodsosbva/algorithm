# from string import digits
# from docutils.utils.math.latex2mathml import letters
from typing import List


class reorder:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)

            else:
                letters.append(log)
        #print(letters)
        #print(digits)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        #digits.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        print(letters)
        print(digits)
        return letters + digits


Reorder = reorder()
k = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(Reorder.reorderLogFiles(k))

