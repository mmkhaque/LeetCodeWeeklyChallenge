class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        if len(arr) == 0:
            return 0
        
        count_elements = collections.Counter(arr)
        least_common = count_elements.most_common()[::-1]

        i = 0
        j = 0
        
        while i !=k:
            
            # item from number
            item = least_common[j][0]
            #number_of_times_appears = least_common[j][1]
            
            #if number_of_times_appears > k:
            #    arr = [x for x in arr if x!=item]
            #    i +=number_of_times_appears
            #else:
                
            while item in arr:
                idx = arr.index(item)
                arr.pop(idx)
                i +=1
                if item not in arr:
                    break
                if i ==k:
                    break
            j +=1

            if i ==k:
                break

        return len(set(arr))
        
            
        
        
        
