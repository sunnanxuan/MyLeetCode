class ExamRoom:

    def __init__(self, n: int):
        self.students = []
        self.n = n

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            return 0
        elif len(self.students) == 1:
            if self.students[0] - 0 >= self.n - 1 - self.students[-1]:
                bisect.insort(self.students, 0)
                return 0
            else:
                bisect.insort(self.students, self.n - 1)
                return self.n - 1
        else:
            sit = [-1, 0]
            if 0 not in self.students:
                sit = [0, self.students[0] - 0]
            pre = self.students[0]
            for i in range(1, len(self.students)):
                c = self.students[i]
                if (c - pre) // 2 > sit[-1]:
                    sit = [pre + (c - pre) // 2, (c - pre) // 2]
                pre = c
            if self.n - 1 not in self.students and self.n - 1 - self.students[-1] > sit[-1]:
                sit = [self.n - 1, self.n - 1 - self.students[-1]]
            bisect.insort(self.students, sit[0])

            return sit[0]

    def leave(self, p: int) -> None:
        self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)