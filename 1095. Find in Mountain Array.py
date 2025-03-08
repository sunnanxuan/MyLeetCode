# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        def findpeak(l, r):
            mid = (l + r) // 2
            a, b, c = mountain_arr.get(mid - 1), mountain_arr.get(mid), mountain_arr.get(mid + 1)
            if a < b > c:
                return mid
            elif a < b < c:
                return findpeak(mid, r)
            elif a > b > c:
                return findpeak(l, mid)

        peak = findpeak(0, n - 1)
        if mountain_arr.get(peak) == target: return peak

        def findtarget(l, r, p):
            while l < r - 1:
                mid = (l + r) // 2
                num = mountain_arr.get(mid)
                if num == target:
                    return mid
                elif num > target:
                    if p == 'L':
                        return findtarget(l, mid, p)
                    elif p == 'R':
                        return findtarget(mid, r, p)
                elif num < target:
                    if p == 'R':
                        return findtarget(l, mid, p)
                    elif p == 'L':
                        return findtarget(mid, r, p)
            return -1

        if mountain_arr.get(0) == target:
            ind_l = 0
        else:
            ind_l = findtarget(0, peak, 'L')
        if mountain_arr.get(n - 1) == target:
            ind_r = n - 1
        else:
            ind_r = findtarget(peak, n - 1, 'R')

        if ind_l == ind_r == -1:
            return -1
        elif ind_l == -1:
            return ind_r
        elif ind_r == -1:
            return ind_l
        else:
            return min(ind_l, ind_r)






