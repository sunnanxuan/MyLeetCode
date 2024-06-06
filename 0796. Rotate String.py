class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):return False
        if set(s)!=set(goal):return False
        if s==goal:return True
        n=len(s)
        for i in range(1,n):
            if s[i:n]==goal[:n-i] and goal[n-i:]==s[:i]:
                return True
        return False