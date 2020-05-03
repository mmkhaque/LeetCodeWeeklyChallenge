class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        l = 0
        
        counter = 0
        
        for idx, num in enumerate(nums):
            
            if num == 0:
                counter +=1
            
            if num == 1:
                if idx == 0:
                    pass
                else:
                    if counter < k:
                        return False
                    else:
                        counter = 0
        
        return True
