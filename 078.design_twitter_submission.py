import heapq

class Twitter:

    def __init__(self):
        self.users = dict()
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        self.users[userId]["tweets"].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.createUser(userId)

        res = []
        minHeap = []   # (timestamp, tweetId, uid, nextIndex)

        self.users[userId]["following"].add(userId)

        # add the most recent tweet of each followee to heap
        for uid in self.users[userId]["following"]:
            tweets = self.users[uid]["tweets"]
            if len(tweets) > 0:
                i = len(tweets) - 1
                timestamp, tweetId = tweets[i]
                heapq.heappush(minHeap, (timestamp, tweetId, uid, i - 1))

        # add most recent tweet to res, and then add the previous tweet
        # by the same user to the heap until the feed is long enough
        while len(minHeap) > 0 and len(res) < 10:
            timestamp, tweetId, uid, idx = heapq.heappop(minHeap)
            res.append(tweetId)

            if idx >= 0:
                nextTimestamp, nextTweetId = self.users[uid]["tweets"][idx]
                heapq.heappush(minHeap, (nextTimestamp, nextTweetId, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.users[followerId]["following"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.users[followerId]["following"].discard(followeeId)
    
    def createUser(self, userId):
        if userId not in self.users:
            self.users[userId] = {
                "tweets": [],    # list of [count, tweetId]s
                "following": set(),   # set of followeeIds
            }
