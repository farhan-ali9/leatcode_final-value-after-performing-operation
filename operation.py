class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        a=len(operations)
        for i in range(a):
            if operations[i]=="--X":
                x=x-1
            elif operations[i]=="X--":
                x=x-1
            elif operations[i]=="X++":
                x=x+1
            else:
                x=x+1
        return x
