class Solution:
    def isValid(self, s: str) -> bool:

        def insert(s):
            if not s:
                return True
            elif 'abc' not in s:
                return False
            else:
                i = s.find('abc')
                return insert(s[:i] + s[i + 3:])

        return insert(s)
