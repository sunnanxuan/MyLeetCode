class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        owner=collections.defaultdict(list)
        for account in accounts:
            name=account[0]
            cur=set(account[1:])
            for m in account[1:]:
                i=0
                while i<len(owner[name]):
                    mail=owner[name][i]
                    if m in mail:
                        cur|=mail
                        owner[name].pop(i)
                    else:
                        i+=1
            owner[name].append(cur)
        res=[]
        for k in owner:
            for l in owner[k]:
                res.append([k]+sorted(list(l)))
        return res