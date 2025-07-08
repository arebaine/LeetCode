from collections import deque
class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.date = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = set()
            self.tweets[userId] = deque([], 10)
        self.tweets[userId].append((tweetId, self.date))
        self.date +=1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = set()
            self.tweets[userId] = deque([], 10)
        feed = []
        for followerid in self.users[userId]:
            feed = feed + list(self.tweets[followerid])
        feed =  feed + list(self.tweets[userId])
        if feed:
            print(feed)
            most_recent = sorted(feed, key = lambda x: x[1])
            if len(most_recent) >= 10:
                return list(zip(*most_recent))[0][-10:][::-1]
            else:
                return list(zip(*most_recent))[0][::-1]
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = set()
            self.tweets[followerId] = deque([], 10)
        if followeeId not in self.users:
            self.users[followeeId] = set()
            self.tweets[followeeId] = deque([], 10)
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = set()
            self.tweets[followerId] = deque([], 10)
        if followeeId not in self.users:
            self.users[followeeId] = set()
            self.tweets[followeeId] = deque([], 10)
        try:
            self.users[followerId].remove(followeeId)
        except:
            pass   
