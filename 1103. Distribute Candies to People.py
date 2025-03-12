class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        n = 1
        i = 0
        while candies:
            if candies < n:
                res[i] += candies
                candies = 0
            else:
                res[i] += n
                candies -= n
                i += 1
                if i == num_people: i = 0
                n += 1
        return res

