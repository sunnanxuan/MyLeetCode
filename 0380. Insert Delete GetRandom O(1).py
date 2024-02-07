class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            return False
        elif val not in self.nums:
            self.nums.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.nums:
            return False
        elif val in self.nums:
            self.nums.remove(val)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        res = choice(self.nums)
        return res