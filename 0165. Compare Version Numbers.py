class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')[::-1]
        v2 = version2.split('.')[::-1]
        while v1 and v2:
            n1 = int(v1.pop())
            n2 = int(v2.pop())
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        while v1:
            if int(v1[0]) == 0:
                v1.pop(0)
            else:
                break
        while v2:
            if int(v2[0]) == 0:
                v2.pop(0)
            else:
                break
        if not v1 and not v2:
            return 0

        elif v1:
            return 1
        elif v2:
            return -1