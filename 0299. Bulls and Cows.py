class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
        dic_s=collections.Counter(secret)
        dic_g=collections.Counter(guess)
        for k in dic_s:
            if k in dic_g:
                cow+=min(dic_s[k],dic_g[k])
        cow-=bull
        return '{}A{}B'.format(bull,cow)