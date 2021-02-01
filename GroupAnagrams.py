import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    print(anagrams)
    return anagrams.values()


InWord = ['eat', 'tea', 'ate', 'tan', 'nat', 'bat']
k = groupAnagrams(InWord)
print(k)
