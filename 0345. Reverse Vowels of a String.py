class Solution:
    def reverseVowels(self, s: str) -> str:
        index=[]
        string=[]
        vowels=[]
        for i,c in enumerate(s):
            if c in 'aeiouAEIOU':
                string.append('#')
                index.append(i)
                vowels.append(c)
            else:
                string.append(c)
        vowels.reverse()
        for i in range(len(vowels)):
            string[index[i]]=vowels[i]
        return "".join(string)