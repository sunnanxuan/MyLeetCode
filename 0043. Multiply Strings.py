class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        n1=0
        for i,s in enumerate(num1[::-1]):
            n1+=dic[s]*10**i
        res=0
        for i,s in enumerate(num2[::-1]):
            res+=n1*dic[s]*10**i
        return str(res)
