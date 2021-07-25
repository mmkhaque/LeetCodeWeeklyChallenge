
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def return_sum(x):
            
            result = 0
            for v in x:
                result += int(v)
                
            return result
            
        
        total = []
        
        for l in s:
            temp = ord(l) - ord('a') + 1
            for v in str(temp):
                total.append(v)
        
        print(total)
        print(return_sum(total))
        
        if k == 1:
            return return_sum(total)
        
        else:
            total = return_sum(total)
            
            print('total ', total)
            
            result = 0 
            
            k -=1
            
            # '33'
            while k != 0:
                
                temp = []
                for v in str(total):
                    temp.append(v)
                result = return_sum(temp)
                k -=1
                total = result
                print('result ', result)

            return result
