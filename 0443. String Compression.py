class Solution:
    def compress(self, chars: List[str]) -> int:
        pre=chars[0]
        n=1
        i=1
        while i <len(chars):
            if chars[i]==pre:
                n+=1
                chars.pop(i)
                if i==len(chars):
                    for s in str(n):
                        chars.insert(i,s)
                        i+=1
            elif chars[i]!=pre:
                if n>1:
                    for s in str(n):
                        chars.insert(i,s)
                        i+=1
                n=1
                pre=chars[i]
                i+=1
        return len(chars)