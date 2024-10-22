from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.count = 0
        self.followeeMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        tweets = []
        self.followeeMap[userId].add(userId)
        for followee in self.followeeMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][index]
                tweets.append([count, tweetId, followee, index])
        heapq.heapify(tweets)
        while len(res) < 10 and len(tweets) > 0:
            count, tweetId, followee, index = heapq.heappop(tweets)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.tweetMap[followee][index - 1]
                heapq.heappush(tweets, [count, tweetId, followee, index - 1])
        return res
 
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)