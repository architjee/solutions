class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        distance_between_prefixes = [[-1]*len(word2) for _ in word1]

        def getDistanceBetweenPrefixes(idx_w1, idx_w2):
            if idx_w1<0:
                return idx_w2+1
            if idx_w2<0:
                return idx_w1+1
            if distance_between_prefixes[idx_w1][idx_w2]==-1:
                if word1[idx_w1]==word2[idx_w2]:
                    distance_between_prefixes[idx_w1][idx_w2]= getDistanceBetweenPrefixes(idx_w1-1, idx_w2-1)
                else:
                    distance_between_prefixes[idx_w1][idx_w2]= 1+ min(getDistanceBetweenPrefixes(idx_w1-1, idx_w2), getDistanceBetweenPrefixes(idx_w1-1, idx_w2-1), getDistanceBetweenPrefixes(idx_w1, idx_w2-1))
            return distance_between_prefixes[idx_w1][idx_w2]
        return getDistanceBetweenPrefixes(len(word1)-1, len(word2)-1)