from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        pairs = []
        
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                
                if nums[i] == nums[j] and i < j:
                    pairs.append([i, j])
                    
        
        print(pairs)
        
        return len(pairs)
