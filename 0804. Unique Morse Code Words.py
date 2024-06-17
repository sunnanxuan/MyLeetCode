class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
               'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
               'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
               'y': '-.--', 'z': '--..'}
        seen = set()
        for word in words:
            arr = []
            for w in word:
                arr.append(dic[w])
            seen.add(''.join(arr))
        return len(seen)
