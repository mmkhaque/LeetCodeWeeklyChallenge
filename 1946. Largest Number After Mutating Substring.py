class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        d = {}
        
        for c in list(num):
            d[int(c)] = change[int(c)]
            
        print(d)
        
        result = int(num)
        
        def integer_value(x):
            
            r = 0
            for d in x:
                r = r * 10 + int(d)
                
            return r
        
        str_num = list(str(num))
        
        print(str_num)
        
        index = 0
        
        old_str_num = str_num
        
        while index < len(str_num):
            
            print('This iteration str num is ', str_num)
            
            
            c = str_num[index]
            
            
            
            print(c, d, ' ->')
            if int(c) in d:
                print(' value of int c ', int(c))
                print('value of d[int(c)] ', d[int(c)])
                str_num[index] = d[int(c)]
                
                print('new str_num ', str_num)
            
                if integer_value(str_num) > result:
                    print('after value conversion interger value is ', integer_value(str_num))
                    result = integer_value(str_num)
                    print('new value of result is ', result)
                    old_str_num = str_num
                    
                else:
                    
                    str_num = old_str_num
                    print('reverting to old str num ', str_num)
            
            
            index +=1
        
        print(result)
        
        return str(result)
        
            
            
            
            
