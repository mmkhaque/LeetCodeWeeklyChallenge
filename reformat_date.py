import re

class Solution:
    def reformatDate(self, date: str) -> str:
        
        month_ = {'Jan': '01', 
                'Feb': '02',
                'Mar' :'03',
                 'Apr' : '04',
                 'May' : '05',
                 'Jun' : '06',
                 'Jul' : '07',
                 'Aug' : '08',
                 'Sep' : '09',
                 'Oct' : '10',
                 'Nov' : '11',
                 'Dec' : '12'
                }
        
        reg_year = '[0-9][0-9][0-9][0-9]'
        
        reg_day = '([0-9]+)[a-z]+'
        
        reg_month = '[A-Z][a-z][a-z]'
        
        reg_year_match = re.search(reg_year, date)
        
        reg_day_match = re.search(reg_day, date)
        
        reg_month_match = re.search(reg_month, date)
        
        month=''
        day = ''
        year = ''
        
        if reg_year_match:
            #print(reg_year_match.group(0))
            year = reg_year_match.group(0)
        
        if reg_day_match:
            #print(reg_day_match.group(0))
            #print(reg_day_match.group(1))
            
            if len(reg_day_match.group(1)) !=2:
                day = '0' + str(reg_day_match.group(1))
            else:
                day = str(reg_day_match.group(1))
            
 
        if reg_month_match:
            print(reg_month_match.group(0))
            
        for k, v in month_.items():
            if k == reg_month_match.group(0):
                month = v
        
        
        print(day, month, year)
        result = str(year) + '-' + str(month) + '-' + str(day)
        
        print(result)
        
        return result
