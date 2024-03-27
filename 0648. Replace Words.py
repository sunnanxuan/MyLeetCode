class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dic={}
        for l in dictionary:
            l+='#'
            cur=dic
            for c in l:
                if c not in cur:
                    cur[c]={}
                cur=cur[c]
        words=sentence.split()
        new=[]
        for word in words:
            cur=dic
            pre=[]
            word+='$'
            for w in word:
                if w not in cur:
                    new.append(word[:-1])
                    break
                else:
                    pre.append(w)
                    cur=cur[w]
                    if '#' in cur:
                        new.append(''.join(pre))
                        break
        return ' '.join(new)