# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.cur = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.cur

    def next(self):
        value = self.cur
        self.cur = self.iterator.next() if self.iterator.hasNext() else None

        return value

    def hasNext(self):
        return self.cur != None
