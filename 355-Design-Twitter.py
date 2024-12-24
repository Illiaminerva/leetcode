from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        feed = []
        heap = []
        for followee in self.follows[userId]:
            if self.tweetMap[followee]:
                index = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][-1]
                heapq.heappush(heap, (count, followee, index, tweetId))
        while len(feed) < 10 and heap:
            count, followee, index, tweetId = heapq.heappop(heap)
            feed.append(tweetId)
            if index > 0:
                count, tweetId = self.tweetMap[followee][index-1]
                heapq.heappush(heap, (count, followee, index-1, tweetId))
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)