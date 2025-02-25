class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        dic = collections.defaultdict(list)
        for i in range(len(values)):
            dic[labels[i]].append(values[i])
        arr = []
        for k in dic:
            dic[k] = sorted(dic[k])
            for _ in range(useLimit):
                if not dic[k]: break
                cur = dic[k].pop()
                if cur <= 0: break
                if len(arr) < numWanted:
                    bisect.insort(arr, cur)
                else:
                    if arr[0] < cur:
                        arr.pop(0)
                        bisect.insort(arr, cur)
                    else:
                        break
        return sum(arr) if arr else 0
