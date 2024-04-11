class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=collections.defaultdict(list)
        for path in paths:
            lst=path.split()
            folder=lst[0]
            for f in lst[1:]:
                name,info=f.split('(')
                dic[info].append('{}/{}'.format(folder,name))
        res=[]
        for k in dic:
            if len(dic[k])>1:
                res.append(dic[k])
        return res