class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        memo = {}

        def count(w):
            if w in memo:
                return memo[w]
            else:
                res = 1
                for i in range(len(w) + 1):
                    for c in string.ascii_lowercase:
                        if w[:i] + c + w[i:] in words_set:
                            res = max(res, 1 + count(w[:i] + c + w[i:]))
                memo[w] = res
                return memo[w]

        words_set = set(words)
        res = 0
        for w in words:
            res = max(res, count(w))
        return res