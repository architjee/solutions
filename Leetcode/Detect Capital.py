class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return all([x.isupper() for x in word]) or all([not x.isupper() for x in word]) or word[0].isupper() and all([x.islower() for x in word[1:]])