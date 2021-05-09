import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        print(counter)

        while True:
            sub_count = 0
            print("hi")
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                print(counter, "res:", result, "sub:", sub_count)

                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
                # print(counter, "res:", result, "sub:", sub_count)

            if not counter:
                break

            result += n - sub_count + 1

        return result


task = ['a', 'a', 'a', 'b', 'b', 'b']
n = 2
sol = Solution()
chk = sol.leastInterval(task, n)
print(chk)