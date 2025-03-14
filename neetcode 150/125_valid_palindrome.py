class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_list = []
        for ch in s:
            if ch.isalnum():
                word_list.append((ch.lower()))
        return word_list == word_list[::-1]
