class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        nums = [0] * n
        
        for i in range(0, n):
            nums[i] = start + 2 * i
            
        res = reduce(lambda x, y : x^y, nums)
        
        return res
