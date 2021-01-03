class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        splitted_array = []
        
        i = 1
        j = 2 
        
        while j < len(nums) and i < j:
            if (sum(nums[0:i]) <= sum(nums[i:j])) and (sum(nums[i:j]) <= sum(nums[j:])):
                splitted_array.append([nums[0:i], nums[i:j], nums[j:]])
            
            j +=1
            
            if j == len(nums):
                i +=1
                j = i+1
   
        return len(splitted_array)
        
                
        
