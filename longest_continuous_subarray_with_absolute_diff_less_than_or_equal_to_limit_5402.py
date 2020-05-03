class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        
        if len(nums) == 0 or not nums:
            return 0

        if len(nums) == 1:
            return 1
        
        if len(set(nums)) ==1:
            return len(nums)
        
        l = 0
        r = 1
        ans = 0
        res = 0
        
        def calculate_diff(nums, l, r, limit):
            
            counter = 0
            
            for i in range(l, r):
                for j in range(l+1, r+1):
                    if abs(nums[i] - nums[j]) > limit:
                        return 0
                    
            return r-l+1
        
        
        while l < r and r < len(nums):
            
            ans = calculate_diff(nums, l, r, limit)
            
            res = max(res, ans)
            if ans!=0:
                
                r +=1
            else:
                l +=1
                r +=1
        
        print(res)
        
        return res
        
