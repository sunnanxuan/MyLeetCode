class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        dic = {}
        letters = string.ascii_lowercase
        for i in range(26):
            dic[i] = letters[i]
            dic[letters[i]] = i
        cur = []
        for c in s:
            cur.append(dic[c])
        sm = sum(shifts)
        res = []
        for i in range(len(s)):
            cur[i] += sm
            cur[i] %= 26
            res.append(dic[cur[i]])
            sm -= shifts[i]
        return ''.join(res)

