class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            ip=queryIP.split('.')
            if len(ip)==4:
                for ad in ip:
                    if ad.isdigit() and 0<=int(ad)<=255 and (len(ad)==1 or ad[0]!='0'):
                        continue
                    else:
                        return "Neither"
                return 'IPv4'
            else:
                return "Neither"
        elif ':' in queryIP:
            ip=queryIP.split(':')
            if len(ip)==8:
                for ad in ip:
                    if 1<=len(ad)<=4 and ad.isalnum():
                        for c in ad:
                            if c not in '0123456789abcdefABCDEF':
                                return "Neither"
                    else:
                        return "Neither"
                return 'IPv6'
            else:
                return "Neither"
        else:
            return "Neither"