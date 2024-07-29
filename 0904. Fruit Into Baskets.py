class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = 0
        dic = collections.defaultdict(int)
        res = 0
        while r < len(fruits):
            if fruits[r] in dic or len(dic) < 2:
                dic[fruits[r]] += 1
                r += 1
            else:
                res = max(res, r - l)
                for k in dic:
                    if k != fruits[r - 1]:
                        p = k
                while dic[p]:
                    dic[fruits[l]] -= 1
                    l += 1
                dic.pop(p)
                dic[fruits[r]] += 1
                r += 1
        res = max(res, r - l)
        return res
