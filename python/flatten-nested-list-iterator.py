# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested_list = nestedList

    def next(self):
        """
        :rtype: int
        """


    def hasNext(self):
        """
        :rtype: bool
        """


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

i, v = NestedIterator([[1,1],2,[1,1]]), []
while i.hasNext(): v.append(i.next())
assert v == [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:

i, v = NestedIterator([1,[4,[6]]]), []
while i.hasNext(): v.append(i.next())
assert v == [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,4,6].