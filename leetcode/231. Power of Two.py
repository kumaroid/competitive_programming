class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = str(bin(n)[2:])
        
        if i.startswith('1') and i.count('1') == 1:
            return True
        return False
        
        
