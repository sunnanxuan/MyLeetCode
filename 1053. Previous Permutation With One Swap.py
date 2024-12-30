class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        ind1 = -1
        ind2 = -1
        for i, c in enumerate(arr):
            new1 = ind1
            new2 = ind2
            for j in range(max(ind1, 0), i):
                if arr[j] <= c:
                    continue
                else:
                    if j > new1:
                        new1, new2 = j, i
                    elif j == new1 and arr[new2] < c:
                        new2 = i
            ind1 = new1
            ind2 = new2
        arr[ind1], arr[ind2] = arr[ind2], arr[ind1]
        return arr



