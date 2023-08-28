class Pessoa:
    def __init__(self, id):
        self.__nome = ""
        self.id = id
    def nome(self):
        return self.__nome
    def nome(self, novoNome):
        self.__nome = novoNome
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
