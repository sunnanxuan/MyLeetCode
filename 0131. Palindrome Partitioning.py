class Solution:
    def partition(self, s: str) -> List[List[str]]:
        q = [[s[0]]]
        n = len(s)
        for i in range(1, n):
            cur = s[i]
            new = []
            for arr in q:
                if arr[-1] == arr[-1][::-1]:
                    new.append(arr + [cur])
                c = arr[-1] + cur
                if i == n - 1 and c == c[::-1]:
                    arr[-1] = c
                    new.append(arr)
                elif i < n - 1 and (len(arr) == 1 or (len(arr) > 1 and arr[-2] == arr[-2][::-1])):
                    arr[-1] = c
                    new.append(arr)
            q = new
        return q

