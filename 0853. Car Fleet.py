class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort()
        res=1
        p,s=cars.pop()
        pre=(target-p)/s
        while cars:
            p,s=cars.pop()
            t=(target-p)/s
            if t>pre:
                res+=1
                pre=t
        return res
