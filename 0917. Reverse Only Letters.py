class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = []
        arr = []
        for i in range(len(s)):
            if s[i].isalpha():
                letters.append(s[i])
            else:
                arr.append((i, s[i]))
        res = []
        c = 0
        while letters:
            if arr and c == arr[0][0]:
                res.append(arr.pop(0)[1])
            else:
                res.append(letters.pop())
            c += 1
        for p, m in arr:
            res.append(m)
        return ''.join(res)

