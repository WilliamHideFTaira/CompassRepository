# Lista animais
animais = ["Pinguim-de-Adélia", "Tartaruga-Marinha", "Orangotango", "Tucano-de-bico-arco-íris", "Suricata", "Lontra", "Guepardo", "Morcego", "Esquilo", "Marsupial", "Quokka", "Leopardo-das-neves", "Rinoceronte", "Elefante", "Camelo", "Urso Polar", "Cavalo-marinho", "Lobo", "Canguru", "Raposa"]

# Ordem crescente
animais.sort()

for animal in animais:
    print(animal)

# Arquivo CSV
with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(animal + "\n")