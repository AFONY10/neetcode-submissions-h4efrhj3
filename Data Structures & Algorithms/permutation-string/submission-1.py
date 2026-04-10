# 1. Hashtable of chars and their no. of occurences
# 2. Expand window and decrement amount of occurences
# 3. Window size = s1 length
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        lp = 0
        rp = lp
        s2Counter = {}
        s1Counter = {}

        # Build Hashtable for s1 for comparison
        for c in s1: 
            if c in s1Counter:
                s1Counter[c] += 1
            else:
                s1Counter[c] = 1
        
        # Build hashtable for s2 and compare
        for rp in range(n2):
            # Hashtable for s2
            if s2[rp] in s2Counter:
                s2Counter[s2[rp]] += 1
            else:
                s2Counter[s2[rp]] = 1
            
            # If currentWindow is same size as length of s1
            if rp - lp + 1 == n1:
                if s2Counter == s1Counter:
                    return True
                else:
                    # Moving window and removing values out of scope
                    s2Counter[s2[lp]] -= 1
                    if s2Counter[s2[lp]] <= 0:
                        s2Counter.pop(s2[lp], None)
                    lp += 1
        
        return False
                
        
           
            

            
                
            
            

            



                
