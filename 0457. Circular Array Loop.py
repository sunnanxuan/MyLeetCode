class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for n in range(len(nums)):
            cur = set()
            if n not in visited:
                if nums[n] > 0:
                    pre = 1
                else:
                    pre = -1
                visited.add(n)
                cur.add(n)
                c = (n + nums[n]) % len(nums)
                if c == n:
                    continue
                while pre * nums[c] > 0:
                    if c in cur and len(cur) > 1:
                        return True
                    else:
                        cur.add(c)
                        visited.add(c)
                        new = (c + nums[c]) % len(nums)
                        if c == new:
                            break
                        else:
                            c = new
        return False
