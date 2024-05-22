class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        ps = bisect.bisect_right(self.calendar, start)
        pe = bisect.bisect_left(self.calendar, end)
        if ps == pe and ps % 2 == 0:
            bisect.insort(self.calendar, start)
            bisect.insort(self.calendar, end)
            return True
        else:
            return False