class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lex={c:chr(i+97) for i,c in enumerate(order)}
        arr=[]
        for i,w in enumerate(words):
            new=[]
            for c in w:
                new.append(lex[c])
            arr.append([''.join(new),i])
        arr.sort()
        inds=[j for k,j in arr]
        return inds==sorted(inds)