class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        self.accounts = accounts
        maxVal = 0

        for i in self.accounts:
                if sum(i) > maxVal:
                    maxVal = sum(i)

        return maxVal
                
acounts = Solution()
print(acounts.maximumWealth([[6,59,64,19,30,76,71,86,90,25,56,17,19,72,61,56,24,40,35,39,67,28,52,11,82,72,8,82,81,47]]))