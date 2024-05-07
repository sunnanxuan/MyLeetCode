class MyLinkedList:

    def __init__(self):
        self.linked_list = []

    def get(self, index: int) -> int:
        if index < len(self.linked_list):
            return self.linked_list[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.linked_list.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.linked_list.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.linked_list):
            self.linked_list.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.linked_list):
            self.linked_list.pop(index)