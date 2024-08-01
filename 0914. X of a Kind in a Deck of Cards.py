class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = collections.Counter(deck)
        arr = list(dic.values())
        arr.sort()
        m = arr[0]
        for i in range(2, m + 1):
            if m % i == 0:
                if all([n % i == 0 for n in arr]): return True
        return False
