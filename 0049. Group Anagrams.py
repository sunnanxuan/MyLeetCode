class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            c = tuple(sorted(collections.Counter(s).items()))
            dic[c].append(s)
        return list(dic.values())
