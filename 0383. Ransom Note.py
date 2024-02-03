class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = collections.Counter(magazine)
        for c in ransomNote:
            if not dic[c]:
                return False
            else:
                dic[c] -= 1
        return True
