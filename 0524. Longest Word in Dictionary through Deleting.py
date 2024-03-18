class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-1*len(x),x))
        for word in dictionary:
            p=0
            for w in word:
                if w not in s[p:]:
                    break
                else:
                    c=s[p:].index(w)
                    p+=(c+1)
            else:
                return word
        return ''
