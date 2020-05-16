class Solution:
    def maxPower(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        i = 0
        j = i+1
        
        mm = 1
        max_mm = 1
        
        while i < j and j < len(s):
            if s[i] == s[j]:
                i +=1
                j +=1
                mm +=1
                max_mm = max(mm, max_mm)
            else:
                i = j
                j = i+1
                mm = 1
        
        print(max_mm)
        
        return max_mm
        
