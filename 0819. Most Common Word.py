class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.split(r"[ !?',;.]", paragraph)
        banned = set(banned)
        dic = collections.defaultdict(int)
        for c in p:
            c = c.lower()
            if c and c not in banned:
                dic[c] += 1
        return sorted(dic.items(), key=lambda x: -1 * x[1])[0][0]
