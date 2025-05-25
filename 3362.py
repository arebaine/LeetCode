from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def maxRemoval(self, nums, queries) -> int:
        count = 0
        good_to_use = []
        used_queries = []
        q = collections.deque(sorted(queries))
        for i, x in enumerate(nums):
            while len(q) > 0 and q[0][0] <= i:
                heapq.heappush(good_to_use, -q[0][1])
                q.popleft()

            while len(used_queries) > 0 and used_queries[0] < i:
                heapq.heappop(used_queries)
            
            while len(good_to_use) > 0 and len(used_queries) < x:
                r = - heapq.heappop(good_to_use)
                if r < i:
                    return -1
                else:
                    count+=1
                    heapq.heappush(used_queries, r)
            if len(used_queries) < x:
                return -1
        return len(queries) - count
