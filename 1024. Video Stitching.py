class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dic = {0: 0}
        arr = [0]
        clips.sort()
        for s, e in clips:
            p = bisect.bisect_left(arr, s)
            if p == len(arr):
                continue
            else:
                cur = 1 + min([dic[arr[i]] for i in range(p, len(arr))])
                if e not in dic:
                    dic[e] = cur
                    bisect.insort(arr, e)
                else:
                    dic[e] = min(dic[e], cur)
        return min([dic[k] for k in dic if k >= time], default=-1)

