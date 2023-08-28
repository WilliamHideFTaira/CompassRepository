class Lampada:
    def __init__ (self, ligada):
        self.ligada = ligada
    def liga(self):
        self.ligada=True
    def desliga(self):
        self.ligada=False
    def esta_ligada(self):
        return self.ligada
lampada = Lampada(True)
lampada.liga()
print("A lâmpada está ligada? {}".format(lampada.esta_ligada()))
lampada.desliga()
print("A lâmpada está ligada? {}".format(lampada.esta_ligada()))