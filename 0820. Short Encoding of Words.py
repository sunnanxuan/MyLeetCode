class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        res=0
        words.sort(key=lambda x:-1*len(x))
        s=set()
        for w in words:
            if w+'#' in s:continue
            else:
                res+=len(w)+1
                for i in range(len(w)):
                    s.add(w[i:]+'#')
        return res