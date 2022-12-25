class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        diff =  collections.Counter(ransomNote)- collections.Counter(magazine)
        print(diff)
        print(not diff)
        return (not diff)