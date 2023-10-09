class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        l = 0
        word = []
        res = []
        for i in range(len(words) + 1):

            if i < len(words) and not word:
                word.append(words[i])
                l += len(words[i])

            elif i < len(words) and l + len(words[i]) + 1 <= maxWidth:
                word.append(words[i])
                l += len(words[i]) + 1
            else:
                if len(word) == 1:
                    res.append(word[0] + ' ' * (maxWidth - l))
                elif i == len(words):
                    res.append(' '.join(word) + ' ' * (maxWidth - l))
                elif maxWidth - l == 0:
                    res.append(' '.join(word))
                else:
                    n = (maxWidth - l) // (len(word) - 1)
                    d = (maxWidth - l) % (len(word) - 1)
                    s = word[0]
                    for c in word[1:]:
                        if d > 0:
                            s += ' ' * (n + 2) + c
                            d -= 1
                        else:
                            s += ' ' * (n + 1) + c
                    res.append(s)
                if i < len(words):
                    word = [words[i]]
                    l = len(words[i])
        return res
