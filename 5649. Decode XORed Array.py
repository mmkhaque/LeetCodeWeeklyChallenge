class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        result = [first]
        
        for x in encoded:
            temp = result[-1]
            result.append(x ^ temp)
            #print(result)
            
        #print(result)
        
        return result
