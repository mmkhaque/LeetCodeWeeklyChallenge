class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        if n == 1:
            return []
        
        simp_frac = []
        
        all_frac = [float(i) for i in range(n)]
        
        fractions = []
        
        for i in range(1, n):
            for j in range(i+1, n+1):
                #print(' > ,', i, j, n)
                if i !=j:
                    num = i
                    de = j
                    #print(num, de, de/num)
                    if num == 1:
                        if str(i) + "/" + str(j) not in simp_frac:
                            if num/de not in fractions:
                                fractions.append(num/de)
                                simp_frac.append(str(i) + "/" + str(j))

                    elif de/num not in all_frac:
                        if str(i) + "/" + str(j) not in simp_frac:
                            if num/de not in fractions:
                                fractions.append(num/de)
                                simp_frac.append(str(i) + "/" + str(j))

        print(fractions)
        print(all_frac)
        print(simp_frac)
        
        
        return simp_frac
        
