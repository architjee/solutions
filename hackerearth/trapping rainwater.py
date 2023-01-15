class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0]
        for x in height:
            pre.append(max(x, pre[-1]))
        post = [0]
        for x in reversed(height):
            post.append(max(x, post[-1]))
        def myreversed(start_idx, end_idx, arr):
            while start_idx<end_idx:
                arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
                start_idx+=1
                end_idx-=1
        myreversed(1, len(post)-1, post)
        print(pre, post)
        water = 0
        for i in range(1, len(pre)):
            water += min(pre[i], post[i])-height[i-1]
        return water