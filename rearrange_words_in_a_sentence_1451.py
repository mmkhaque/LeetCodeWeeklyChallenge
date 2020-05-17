class Solution:
    def arrangeWords(self, text: str) -> str:
        
        if len(text) <=1:
            return text
        
        words = str(text).split(' ')
        
        first_word = words[0]
        
        print('total words ', words)
        print('first word ', first_word)
        
        wd = collections.defaultdict(list)
        
        for w in words:
            wd[len(w)].append(w)
            #print(' print dict ', w, wd)
        
        sorted_keys = sorted(wd.keys())
        
        result = []
        
        for key in sorted_keys:
            l  = wd[key]
            #print('l ', l, wd[key], len(l), type(l))
            if len(l) == 1:
                #print('list is of length 1')
                if l[0] == first_word:
                    if len(result) > 1:
                        result.append(''.join(l[0].lower()))
                    else:
                        result.append(''.join(l[0]).lower())
                else:
                    if len(result) == 0:
                        result.append(''.join(l[0].lower()))
                    else:
                        result.append(''.join(l[0].lower()))
                #print('result ', result)
                
            elif len(l) > 1:
                for i in range(0, len(l)):
                    if l[i] == first_word:
                        if len(result) > 1:
                            result.append(''.join(l[i].lower()))
                        else:
                            result.append(''.join(l[i].lower()))
                    else:
                        if len(result) == 0:
                            result.append(''.join(l[i].lower()))
                        else:
                            result.append(''.join(l[i].lower()))
                        
        print(result)
        first_word = result.pop(0)
        first_word = str(first_word).capitalize()
        result.insert(0, first_word)
        
        ans = str(' '.join(result))
        
        print(ans)
        
        return ans
        
        
