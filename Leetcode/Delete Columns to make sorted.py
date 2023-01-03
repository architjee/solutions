class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ## I am assuming that all strings are of equal length.
        my_array = [iter(each_string) for each_string in strs]
        delete_cols = 0
        for i in range(len(strs[0])):
            col_data =[]
            for any_iter in my_array:
                col_data.append(next(any_iter))
            if col_data==sorted(col_data):
                pass
            else:
                delete_cols+=1
        
        return delete_cols