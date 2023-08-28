## Sprint 3

A Sprint 3 é focada totalmente em Python, linguagem de programação simples e sólida para engenheiros de dados que desejam coletar, processar, analizar e visualizar dados de maneira eficaz e eficiente. Sua versatilidade e rica ecossistema de bibliotecas tornam-no uma linguagem poderosa para a engenharia de dados.

### **Python**

Python é uma linguagem de programação de alto nível que se destaca por sua simplicidade e legibilidade. Abaixo estão alguns conceitos-chave em Python:

#### **Variáveis**

Python trabalha com diversos tipos de variáveis:

* **int** - armazena um valor inteiro;
* **float** - armazena um valor de ponto flutuante (número decimal);
* **str** - armazena uma sequência de caracteres (texto);
* **bool** - armazena um valor booleano (True ou False).

Exemplo:
```
numero_inteiro = 10
numero_decimal = 3.14
texto = "Olá, mundo!"
verdadeiro = True
```

#### **Estruturas de Controle**

Python possui estruturas de controle de fluxo para tomada de decisões e repetição:

* **if** - permite tomar decisões condicionais;

```
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

* **for** - ausado para loops definidos (iteração sobre uma sequência);

```
for i in range(5):
    print(i)
```

* **while** - usado para loops indefinidos (enquanto uma condição for verdadeira);

```
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

#### **Coleções de Dados**

Python oferece várias estruturas de dados, incluindo:

* **Listas** - Sequências mutáveis de elementos;
* **Tuplas** - Sequências imutáveis de elementos;
* **Dicionários** - Armazenam pares chave-valor;
* **Conjuntos** - Coleções únicas de elementos.

#### **Funções**

Funções permitem organizar código em blocos reutilizáveis:

```
def saudacao(nome):
    return "Olá, " + nome + "!"

mensagem = saudacao("Maria")
print(mensagem)
```

#### **Módulos**

Python possui uma ampla biblioteca padrão e permite importar módulos externos:

```
import math
print(math.sqrt(16))  # Calcula a raiz quadrada de 16
```

#### **Orientação a Objetos**

Python suporta programação orientada a objetos:

```
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

rex = Cachorro("Rex")
print(rex.fazer_som())  # Saída: "Au Au"
```

#### **Tratamento de Exceções**

Python permite o tratamento de exceções para lidar com erros de forma elegante:

```
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")
```

Estas são apenas algumas das muitas funcionalidades que Python oferece. A linguagem é versátil e amplamente utilizada em desenvolvimento web, científico e automação, tornando-a uma ótima escolha para aprender e criar uma variedade de projetos.