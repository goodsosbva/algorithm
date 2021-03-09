import collections


def topKFrequent(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


nums = [1, 1, 1, 2, 2, 3]
k = 2
res = topKFrequent(nums, k)
print(res)

i = list(zip(collections.Counter(nums).most_common(2)))
print(i)