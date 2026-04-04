from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anamap = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anamap[sorted_word].append(word)
        
        return (anamap.values())