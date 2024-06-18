class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def splitword(s):
            arr=[]
            pre=''
            n=0
            for i in range(len(s)):
                if s[i]==pre:
                    n+=1
                else:
                    if n:arr.append(pre*n)
                    pre=s[i]
                    n=1
            arr.append(pre*n)
            return arr
        res=0
        arr_s=splitword(s)
        for w in words:
            arr_w=splitword(w)
            if len(arr_w)!=len(arr_s):continue
            for i in range(len(arr_s)):
                if arr_s[i][0]!=arr_w[i][0] or len(arr_s[i])<len(arr_w[i]) or len(arr_s[i])<3 and len(arr_s[i])!=len(arr_w[i]):break
            else:res+=1
        return res