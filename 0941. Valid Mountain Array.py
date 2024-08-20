class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = False
        if len(arr) < 3 or arr[1] <= arr[0]: return False
        for i in range(1, len(arr)):
            if not peak:
                if arr[i] < arr[i - 1]:
                    peak = True
                elif arr[i] == arr[i - 1]:
                    return False
            else:
                if arr[i] >= arr[i - 1]: return False
        return peak
