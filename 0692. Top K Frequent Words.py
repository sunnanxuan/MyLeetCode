class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = collections.Counter(words)
        arr = sorted([k for k in dic], key=lambda x: (-1 * dic[x], x))
        return arr[:k]
