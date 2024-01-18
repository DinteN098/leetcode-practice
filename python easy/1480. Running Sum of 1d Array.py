def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []

        for i in range(len(nums)):
            if len(ans) == 0:
                ans.append(nums[i])
            else:
                ans.append(ans[-1] + nums[i])
        return ans