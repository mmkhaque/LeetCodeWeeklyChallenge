class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        if len(deliciousness) == 0:
            return 0
        
        max_limit = 0
        
        deliciousness.sort()
        
        max_limit = deliciousness[-1] + deliciousness[-2]
        
        # power of two list
        pot_list = []
        
        value = 2
        
        while value <= max_limit:
            pot_list.append(value)
            value *= 2
        
        #print(pot_list)
        
        #print(max_limit)
        value = 2
        
        i, j = 0, 1
        max_limit = len(deliciousness)
        
        result = []
        
        while j < max_limit: # and i < j:
            
            #print(i, j)
            total = deliciousness[i] + deliciousness[j]
            
            if total in pot_list:
                #print(deliciousness[i], deliciousness[j], total, i, j)
                if [i,j] not in result:
                    result.append([i,j]) 
            j +=1
            
            if j == max_limit:
                i +=1
                j = i+1
        
        #print(result)
        
        return len(result)
            
        '''
        
        
        d = collections.defaultdict(list)
        
        for index, num in enumerate(deliciousness):
            l = []
            for pot in pot_list:
                l.append(pot-num)
            l.append(index)
            d[num].extend(l)
        
        for k, v in d.items():
            print(k, v)
        '''     
        
