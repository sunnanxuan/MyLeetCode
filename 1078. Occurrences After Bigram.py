class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        dic_ind = {}
        f_ind = []
        for i, c in enumerate(text):
            dic_ind[i] = c
            if c == first: f_ind.append(i)

        res = []
        for i in f_ind:
            if i + 1 in dic_ind and dic_ind[i + 1] == second:
                if i + 2 in dic_ind: res.append(dic_ind[i + 2])
        return res


