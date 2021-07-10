class Test:
    def __init__(self, vala, valb):
        self.vala = vala
        self.valb = valb

    def prt(self):
        print(self)
        print(self.__class__)


t = Test(1, 2)
t.prt()
print(Test.__dict__)
