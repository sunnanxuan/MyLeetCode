class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        dic_p = {}
        dic_s = {}
        for i in range(len(s)):
            if pattern[i] not in dic_p and s[i] not in dic_s:
                dic_p[pattern[i]] = s[i]
                dic_s[s[i]] = pattern[i]
            elif (pattern[i] in dic_p and dic_p[pattern[i]] != s[i]) or (s[i] in dic_s and dic_s[s[i]] != pattern[i]):
                return False
        return True
