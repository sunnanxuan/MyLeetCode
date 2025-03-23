class Solution:
    def defangIPaddr(self, address: str) -> str:
        add = address.split('.')
        return '[.]'.join(add)
