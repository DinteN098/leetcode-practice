class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        self.jewels = jewels
        self.stones = stones

        count = 0

        for i in self.stones:
            if i in self.jewels:
                count += 1

        return count