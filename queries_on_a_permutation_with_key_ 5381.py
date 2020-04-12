
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        
        if m == 0 or len(queries) == 0:
            return []
        
        index_array = [i+1 for i in range(m)]
        
        print(index_array)
        
        start = 0
        result = []

        while start < len(queries):
            
            print('>', start, '<')
            num = queries[start]
            result.append(index_array.index(num))
            index_array.remove(num)
            index_array.insert(0, num)
            start +=1
   
        return result
            
            
            
        
        
