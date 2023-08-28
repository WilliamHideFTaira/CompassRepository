class Calculo:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def soma(self):
        return self.X + self.Y
    def subtrai(self):
        return self.X - self.Y
x = 4
y = 5
calculo = Calculo(x, y)
print("Somando: {}+{} = {}".format(x, y, calculo.soma()))
print("Subtraindo: {}-{} = {}".format(x, y, calculo.subtrai()))