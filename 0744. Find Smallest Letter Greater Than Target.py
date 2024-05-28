class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        p = bisect.bisect_right(letters, target)
        if p == len(letters):
            return letters[0]
        else:
            return letters[p]
