class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        if len(words) == 0 or words is None:
            return 0
        
        #words.sort()
        
        print(words)
        
        matched_words = [False] * len(words)
        
        result = []
        
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    if matched_words[i] == False:
                        matched_words[i] = True  
                        result.append(words[i])
                elif words[j] in words[i]:
                    if matched_words[j] == False:
                        matched_words[j] = True
                        result.append(words[j])
                        
        
        print(result)
        
        return result
                
