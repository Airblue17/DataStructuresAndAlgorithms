# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:54:00 2020

@author: nitin
"""

import heapq as hq

class Users(object):
    def __init__(self, userID):
        self.userID = userID
        self.newsFeed = None
        self.tweets = []
        self.following = {}
        self.followers = {}
        
    def addTweet(self, tweetID, followeeTweet= False):
        if not self.newsFeed:
            self.newsFeed = []
            hq.heappush(self.newsFeed, tweetID)
            if not followeeTweet:
                self.tweets = [tweetID]
            return
        hq.heappush(self.newsFeed, tweetID)
        if not followeeTweet:
            self.tweets.append(tweetID)
        

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.tweets = []
        
    def addUserIfnotExists(self, userId):
        if userId not in self.users:
            self.users[userId] = Users(userId)
        
    def updateFollowersNewsFeed(self, user, tweetId):
        for follower in user.followers:
            follower.addTweet(tweetId, followeeTweet = True)
        
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.addUserIfnotExists(userId)
        user = self.users[userId]
        self.tweets.append(tweetId)
        currTweetIdx = len(self.tweets)-1
        user.addTweet(currTweetIdx)
        self.updateFollowersNewsFeed(user, currTweetIdx)
        
    def addnewFolloweeTweets(self, follower, followee):
        for tweet in followee.tweets:
            follower.addTweet(tweet, followeeTweet = True)
     
    def removeUnfollowedUserTweets(self, user, unfollowedUser):
        if not unfollowedUser.tweets:
            return
        for tweet in unfollowedUser.tweets:
            user.newsFeed.remove(tweet)
            
        hq.heapify(user.newsFeed)
            
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self.addUserIfnotExists(userId)
        user = self.users[userId]
        if not user.newsFeed:
            return []
        tweetIdxs = hq.nlargest(10, user.newsFeed) 
        return [self.tweets[tweetIdx] for tweetIdx in tweetIdxs]  

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.addUserIfnotExists(followerId)
        self.addUserIfnotExists(followeeId)
        follower = self.users[followerId]
        followee = self.users[followeeId]
        if followerId == followeeId:
            return
        if followee in follower.following:
            return
        follower.following[followee] = 1
        followee.followers[follower] = 1
        self.addnewFolloweeTweets(follower, followee)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.addUserIfnotExists(followerId)
        self.addUserIfnotExists(followeeId)
        follower = self.users[followerId]
        followee = self.users[followeeId]
        if followerId == followeeId:
            return
        if followee not in follower.following:
            return
        self.removeUnfollowedUserTweets(follower, followee)
        del follower.following[followee] 
        del followee.followers[follower] 
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)