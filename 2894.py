class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        m1 = 0
        m2 = 0
        for i in range(1, n+1):
            if i%m == 0:
                m2+=i
            else:
                m1+=i
        return m1 - m2
