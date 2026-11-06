class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        win=s[0:k]
        vowels={'a','e','i','o','u'}
        cnt=0
        for ch in win:
            if ch in vowels:
                cnt+=1
        m=cnt
        l=0
        for r in range(k,len(s)):
            if s[r] in vowels:
                cnt+=1
            if s[l] in vowels:
                cnt-=1
            m=max(m,cnt)
            l+=1
        return m 


        
