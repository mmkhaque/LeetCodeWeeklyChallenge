class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        def calculate_median(arr):
            n = len(arr)
            med = (n-1)/ 2
            
            return arr[int(med)]
        
        if len(arr) == 0:
            return []
        
        if k == 0:
            return []
        
        arr.sort()
        med = calculate_median(arr)

        ans = []
        
        for index, num in enumerate(arr):
            ans.append([num, abs(num-med), index])
        
        ans.sort(key=lambda x: (x[1], x[2]), reverse=True)
        
        output = []
        
        i = 0
        j = 1
        
        i = 0
        for num, diff, index in ans:
            i +=1
            output.append(num)
            if i == k:
                break
        
        return output
        
        
