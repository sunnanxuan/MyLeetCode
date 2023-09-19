class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        q = []
        for d in digits:
            if not q:
                for c in dic[d]:
                    q.append(c)

            else:
                new = []
                for l in q:
                    for c in dic[d]:
                        new.append(l + c)
                q = new
        return q