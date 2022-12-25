class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def directed_partitioning(offset, partial_partition):
            if offset==len(s):
                result.append(partial_partition.copy())
                return
            for i in range(offset+1, len(s)+1):
                prefix = s[offset: i]
                if prefix==prefix[::-1]:
                    directed_partitioning(i, partial_partition+[prefix])
        directed_partitioning(0, [])
        return result