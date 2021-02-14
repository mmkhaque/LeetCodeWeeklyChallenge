class Solution:
    def minOperations(self, s: str) -> int:
        
        # alternating
        a = 0
        
        if len(s) <= 1:
            return 0
        
        if len(s) == 2:
            if len(collections.Counter(s)) == 2:
                return 0
        
        s_ = list(s)
        
        l = len(s_)
        
        def flip_string(c):
            if c == '0':
                return '1'
            else:
                return '0'
        
        
        def get_flips(s, next):
            
            counter = 0
            for i in range(len(s)):
                
                if s[i] != next:
                    counter +=1
                
                next = flip_string(next)
            
            return counter
        
        
        return min(get_flips(s, '0'), get_flips(s, '1'))
        '''
        for i in range(l-1):
            
            if s_[i] == s_[i+1]:
                if s_[i+1] == '0':
                    s_[i+1] = '1'
                elif s_[i+1] == '1':
                    s_[i+1] = '0'
                a +=1
                
            print(s_)
        
        '''
        
        #print(a)
        
        #return a
        
