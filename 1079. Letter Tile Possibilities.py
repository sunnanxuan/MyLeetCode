class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seq = set()
        for i in range(1, len(tiles) + 1):
            for each in itertools.permutations(tiles, i):
                seq.add(tuple(each))
        return len(seq)
