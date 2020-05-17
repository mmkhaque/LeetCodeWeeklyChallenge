class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        if queryTime == 0:
            return len(startTime)
        
        if not queryTime:
            return 0
        
        count = 0
        
        for i in range(0, len(startTime)):
            if (queryTime >= startTime[i]) and (queryTime <= endTime[i]):
                count +=1
                
        print(count)
        
        return count
