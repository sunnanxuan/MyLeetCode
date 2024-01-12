class Solution:
    def numberToWords(self, num: int) -> str:
        ones={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        digit={100:'Hundred',1000:'Thousand',1000000:'Million',1000000000:'Billion'}
        f=[1000000000,1000000,1000,100]
        def convert(n):
            if n==0:
                return 'Zero'
            elif n<20:
                return ones[n]
            else:
                d=n%10
                p=(n//10)*10
                if d==0:
                    return ones[p]
                else:
                    return ones[p]+' '+ones[d]


        res=[]
        if num<100:
            res.append(convert(num))
        else:
            for d in f:
                if num<d:
                    continue
                else:
                    n=num//d
                    res.append(self.numberToWords(n))
                    res.append(digit[d])
                    num%=d
            if num!=0:
                res.append(convert(num))
        return ' '.join(res)