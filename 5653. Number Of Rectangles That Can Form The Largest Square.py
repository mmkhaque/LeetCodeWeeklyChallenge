class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        if len(rectangles) == 0:
            return 0
        
        max_len_arr = [min(x) for x in rectangles]
        
        #print(max_len_arr)
        
        result = collections.Counter(max_len_arr)
        max_result = max(result)
        #print(max_result)
        
        print(result[max_result])
        
        return result[max_result]
