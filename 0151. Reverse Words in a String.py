class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        lst.reverse()
        res=' '.join(lst)
        return res
