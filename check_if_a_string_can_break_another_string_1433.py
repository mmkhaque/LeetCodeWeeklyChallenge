class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        if not s1 or not s2:
            return False
        
        if len(s1) == 0 or len(s2) == 0:
            return 0
        
        def sorted_ascii(s):
            
            res = [0] * len(s)
            s_list = list(s)
            for idx, item in enumerate(s_list):
                res.append(ord(item))
            
            res.sort()
            return res
        
        s1_ascii = sorted_ascii(s1)
        s2_ascii = sorted_ascii(s2)
        
        def compare(s1, s2):
            for i in range(0, len(s1)):
                if s1[i] < s2[i]:
                    return False
            return True

        
        if compare(s1_ascii, s2_ascii) or compare(s2_ascii, s1_ascii):
            return True
        
        return False
