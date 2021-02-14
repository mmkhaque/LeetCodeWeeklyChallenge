class Solution:
    def countHomogenous(self, s: str) -> int:
        
        def find_total(number):
            
            counter = 0
            value = 1
            
            while number !=0:
                counter += value
                value +=1
                number -=1
            
            return counter
         
        #consecutive_char = {'1': 1, '2': 3, '3': 6, '4': 10, '5': 15, '6':21}
               
        counter = 0
        
        # total number of characters in the string are
        #c = collections.Counter(s)
        
        # if we have only 1 value
        if len(set(s)) == 1:
            return find_total(len(s))
        
        temp_count = 0
        tokens = list(s)
        i = 0
        
        while i != len(tokens)-1:
            
            if tokens[i] != tokens[i+1]:
                temp_count +=1
                counter += find_total(temp_count)
                temp_count = 0
            else:
                temp_count +=1
            
            i +=1
        
        temp_count +=1
        print('final temp count value ', temp_count)
        if temp_count !=0:
            counter += find_total(temp_count)
            
        print(counter)
        
        return counter
            
