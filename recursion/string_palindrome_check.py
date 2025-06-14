class Solution:
    def palindromeCheck(self, s, i=0):
        if i >= len(s) / 2:  
            return True
        if s[i] != s[len(s) - 1 - i]: 
            return False
        return self.palindromeCheck(s, i + 1)  
    
sol = Solution()
print(sol.palindromeCheck('aabbaaa'))  
print(sol.palindromeCheck('racecar')) 