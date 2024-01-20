class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """

        self.hours = hours
        self.target = target

        ans = []

        for i in self.hours:
            if i >= self.target:
                ans.append(self.hours.index(i)+1)

        return len(ans)