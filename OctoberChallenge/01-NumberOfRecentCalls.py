class RecentCounter:

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        count = 0
        delete = 0
        for i in range(len(self.times)):
            if self.times[i] < t - 3000:
                delete = i + 1
        del self.times[:delete]
        return int(len(self.times))