class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        #if sorted(prices) == prices:
        #    return prices
        
        if len(prices) == 0:
            return []
        
        i = 0
        j = 1
        
        while j < len(prices) and i < j:
            
            if prices[i] >= prices[j] and j > i:
                prices[i] -= prices[j]
                i +=1
                j = i+1

            elif j == len(prices) -1:
                #print(j, len(prices)-1)
                i +=1
                j = i +1
            elif prices[i] < prices[j]:
                j +=1
                
            #print(i, j, prices, len(prices)-1)
            
        print(prices)
        
        return prices
            
            
