'''
https://leetcode.com/contest/weekly-contest-223/problems/minimize-hamming-distance-after-swap-operations/
'''

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        
        def find_diff(source, target):
            output = 0
            
            for a, b in zip(source, target):
                print(a, b)
                if a !=b:
                    output += 1
            return output
        
        
        if len(allowedSwaps) == 0:
            return find_diff(source, target)
        
        d = {}
        
        for x in allowedSwaps:
            d[source[x[0]]] = source[x[1]]
            d[source[x[1]]] = source[x[0]]
        
        for k, v in d.items():
            print(k, ' => ', v)
                
        output = 0
        
        swapped_letter = []
        
        source2 = [0] * len(source)
        
        i = 0
        while i < len(source):
            
            print(source[i], target[i])
            if source[i] == target[i]:
                pass
                print(source[i], target[i], ' are same')
            elif source[i] in d:
                if d[source[i]] == target[i]:
                    if source[i] not in swapped_letter or target[i] not in swapped_letter:
                        #print(source[i], target[i], ' are swapped')
                        j = source.index(target[i])
                        print(' before ', source)
                        source[i], source[j] = source[j], source[i]
                        print(' after ', source)
                        swapped_letter.append(target[i])
                        swapped_letter.append(source[i])
            else:
                output +=1
            i +=1
        
        print('after swapping done new values of source')
        print(source, target)
        
        
                    
        output = find_diff(source, target)
        
        return output
                
        
