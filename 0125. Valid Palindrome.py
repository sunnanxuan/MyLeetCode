class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if c.islower() or c.isdigit():
                arr.append(c)
            elif c.isupper():
                arr.append(c.lower())
            else:
                continue
        ns = ''.join(arr)
        return ns == ns[::-1]
