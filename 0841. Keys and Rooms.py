class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlock=set()
        q={0}
        while q:
            new=set()
            for k in q:
                if k not in unlock:
                    unlock.add(k)
                    new|=set(rooms[k])
            q=new
        return len(unlock)==len(rooms)