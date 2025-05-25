class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = []
        for x in nums:
            delta.append((x^k) - x)
        
        delta.sort(reverse=True)
        count = sum(nums)
        for i in range(0, len(nums), 2):
            if i+1 >= len(nums):
                continue 
            if delta[i] + delta[i+1] > 0:
                count+= (delta[i] + delta[i+1])
        return count
