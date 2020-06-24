# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:52:25 2020

@author: nitin
"""

import heapq as hq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.stream = nums
        hq.heapify(self.stream)
        while len(self.stream) > k:
            hq.heappop(self.stream)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.stream)<self.k:
            hq.heappush(self.stream, val)
        elif val>self.stream[0]:
            hq.heapreplace(self.stream, val)
        return self.stream[0] 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)