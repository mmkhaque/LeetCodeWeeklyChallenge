class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        if len(sentence) == 0:
            return -1
        
        if len(searchWord) == 0:
            return -1
        
        sentence_ = str(sentence).split(" ")
        
        print(sentence_)
        
        for index, s in enumerate(sentence_):
            if str(s).startswith(searchWord):
                return index+1
        
        return -1
