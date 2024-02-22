class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        seen = set()

        def change(gene, n):
            seen.add(gene)
            if gene == endGene:
                res[0] = min(res[0], n)
            elif n < res[0]:
                for i in range(8):
                    for s in 'ACGT':
                        new = gene[:i] + s + gene[i + 1:]
                        if new in bank and new not in seen:
                            change(new, n + 1)

        res = [float('inf')]
        if endGene not in bank:
            return -1
        change(startGene, 0)
        if res[0] == float('inf'):
            return -1
        else:
            return res[0]
