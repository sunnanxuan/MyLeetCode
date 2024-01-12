class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n=0
        for c in citations:
            if c>=(n+1):
                n+=1
            else:
                break
        return n