class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        if n == 0:
            return []
        
        ans = []
        
        i = 0
        
        while n < len(nums):
            ans.append(nums[i])
            ans.append(nums[n])
            i +=1
            n +=1
            
        print(ans)
        
        return ans
            
