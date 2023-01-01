class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        new_set = set()
        i=0
        string_split = s.split()
        if len(pattern)==len(string_split):
            pass
        else:
            return False
        while i<len(pattern):
            if pattern[i] in d and d[pattern[i]]==string_split[i]:
                i+=1
                continue
            elif pattern[i] not in d:
                if string_split[i] in new_set:
                    return False
                new_set.add(string_split[i])
                d[pattern[i]]=string_split[i]
            elif pattern[i] in d and d[pattern[i]]!=string_split[i]:
                return False
            i+=1
        return True
        