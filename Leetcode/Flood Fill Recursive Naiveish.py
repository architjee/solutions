class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, incomingColor: int) -> List[List[int]]:
        if image[sr][sc]==incomingColor:
            return image;
        def flood(image, sr, sc, testColor, replacementColor):
            if sr>=0 and sr<len(image) and sc>=0 and sc<len(image[0]) and image[sr][sc]==testColor:
                image[sr][sc]=replacementColor
                flood(image, sr+1, sc, testColor, replacementColor)
                flood(image, sr-1, sc, testColor, replacementColor)
                flood(image, sr, sc+1, testColor, replacementColor)
                flood(image, sr, sc-1, testColor, replacementColor)
        flood(image, sr, sc, image[sr][sc], incomingColor)
        return image