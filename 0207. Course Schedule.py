class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=collections.defaultdict(list)
        net=collections.defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
            net[b].append(a)
        done=set()
        change=True
        while change:
            change=False
            for i in range(numCourses):
                if not pre[i] and i not in done:
                    change=True
                    done.add(i)
                    for c in net[i]:
                        pre[c].remove(i)
        return len(done)==numCourses