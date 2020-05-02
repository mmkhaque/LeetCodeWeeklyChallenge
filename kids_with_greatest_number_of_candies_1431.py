class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        if len(candies) == 0 or not candies:
            return [False]
        
        max_candies = max(candies)
        
        res = [False] * len(candies)
        
        for index, candi in enumerate(candies):
            if candi + extraCandies >= max_candies:
                res[index] = True
        
        print(res)
        
        return res
            
        
