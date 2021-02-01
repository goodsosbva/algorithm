import collections
import operator
import re
from typing import List


def mostCommomWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
             if word not in banned]
    counts = []
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    sdict = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    return sdict[0]
    # counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    # return counts.most_common(1)[0][0]


paragraph = "음식이 많이 식음, 맛만보고 훅가,음식이 제일좋아!"
banned = ["맛"]
boolis = mostCommomWord(paragraph, banned)
print(boolis)
