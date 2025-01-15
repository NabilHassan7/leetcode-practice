from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_map = defaultdict(list)
        for str in strs:
            sorted_word = "".join(sorted(str))
            word_map[sorted_word].append(str)
        return list(word_map.values())
