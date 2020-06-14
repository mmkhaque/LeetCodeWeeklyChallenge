class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        i = 1
        
        while i < len(nums):
            nums[i] = nums[i-1] + nums[i]
            i +=1
            
        print(nums)
        
        return nums
        
