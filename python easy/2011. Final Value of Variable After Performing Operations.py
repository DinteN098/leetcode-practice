class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        self.operations = operations
        x = 0

        for i in self.operations:
            if "+" in i:
                x += 1
            elif "-" in i:
                x -= 1

        return x
