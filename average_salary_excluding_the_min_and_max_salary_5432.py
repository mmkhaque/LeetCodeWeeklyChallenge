class Solution:
    def average(self, salary: List[int]) -> float:
        
        if len(salary) == 0:
            return 0
        
        salary.sort()
        
        salary.pop(0)
        salary.pop(-1)
        
        return sum(salary) / len(salary)
