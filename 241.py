from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    # print(left, right, op)
                    results.append(eval(str(l) + op + str(r)))
            return results

        # print(input)
        if input.isdigit():  # 하나의 숫자가 들어온 경우
            # print(input)
            return [int(input)]

        results = []
        # print(list(enumerate(input)))
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                print(left, right)

                results.extend(compute(left, right, value))
        return results


texts = "2*3-4*5"
sol = Solution()
chk = sol.diffWaysToCompute(texts)
print(chk)
