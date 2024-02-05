class Twitter:

    def __init__(self):
        self.user = collections.defaultdict(list)
        self.followee = collections.defaultdict(set)
        self.n = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user[userId].append([self.n, tweetId])
        if len(self.user[userId]) > 10:
            self.user[userId].pop(0)
        self.n += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = []
        arr.extend(self.user[userId])
        for c in self.followee[userId]:
            arr.extend(self.user[c])
        arr.sort(reverse=True)

        return [t for n, t in arr[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].discard(followeeId)

