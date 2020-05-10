class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        if n == 0:
            return [""]
        
        if target == [1] and n == 1:
            return ['Push']
        
        ans = []
        
        for i in range(1, target[-1]+1):
            ans.append('Push')
            
            if i not in target:
                ans.append('Pop')
            
            if i == target[-1]:
                break
        
        return ans
            
