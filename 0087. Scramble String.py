class Solution:
    def isScramble(self, s1, s2):
        memo={}
        def swap(s1,s2):
            if (s1,s2) in memo:
                return memo[(s1,s2)]
            if s1==s2:
                memo[(s1,s2)]=True
                return True
            elif len(s1)==1:
                memo[(s1,s2)]=False
                return False

            if any((swap(s1[:i],s2[:i]) and swap(s1[i:],s2[i:])) or (swap(s1[:i],s2[-i:]) and swap(s1[i:],s2[:-i]))  for i in range(1,len(s1))) :
                memo[(s1,s2)]=True
                return True
            else:
                memo[(s1,s2)]=False
                return False
        return swap(s1,s2)

