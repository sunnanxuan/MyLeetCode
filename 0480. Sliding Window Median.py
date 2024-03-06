class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        win = sorted(nums[:k])
        res = []
        if k % 2:
            res.append(win[k // 2])
        else:
            res.append((win[k // 2 - 1] + win[k // 2]) / 2)
        for i in range(k, len(nums)):
            win.remove(nums[i - k])
            bisect.insort(win, nums[i])
            if k % 2:
                res.append(win[k // 2])
            else:
                res.append((win[k // 2 - 1] + win[k // 2]) / 2)
        return res
