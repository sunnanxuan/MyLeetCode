class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:return 0
        used=set()
        used.add(beginWord)
        heap=[(1,beginWord)]
        heapq.heapify(heap)
        while heap:
            n,w=heapq.heappop(heap)
            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    new=w[0:i]+c+w[i+1:]
                    if new==endWord:return n+1
                    if new in wordList and new not in used:
                        heapq.heappush(heap,(n+1,new))
                        used.add(new)
        return 0

