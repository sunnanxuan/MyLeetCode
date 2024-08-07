class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for n in nums:
            if n % 2:
                odds.append(n)
            else:
                evens.append(n)
        res = []
        while odds:
            res.append(evens.pop())
            res.append(odds.pop())
        return res
