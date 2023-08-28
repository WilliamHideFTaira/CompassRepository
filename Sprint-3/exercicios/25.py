class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "Azul"
        self.capacidade = capacidade
aviao1 = Aviao("BOIENG456", 1500, 400)
aviao2 = Aviao("Embraer Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)

avioes = [aviao1, aviao2, aviao3]

for i in avioes:
    print(f"O avião de modelo \"{i.modelo}\" possui uma velocidade máxima de \"{i.velocidade_maxima}\", capacidade para \"{i.capacidade}\" e é da cor \"{i.cor}\".")
