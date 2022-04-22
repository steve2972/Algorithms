class Fancy:

    def __init__(self):
        self.list = list()
        self.mod = 10 ** 9 + 7
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        adjusted_val = (val - self.add) * pow(self.mul, -1, self.mod)
        self.list.append(adjusted_val)

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add = self.add * m % self.mod
        self.mul = self.mul * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx > len(self.list)-1: return -1
        return int((self.mul * self.list[idx] + self.add) % self.mod)