import hashlib

while True:
    # Recebe uma string
    texto = input("Digite uma palavra para gerar o hash (Ctrl+C para sair): ")

    # Gerar o hash
    sha1 = hashlib.sha1()
    sha1.update(texto.encode())
    hashRes = sha1.hexdigest()

    # Imprimir o hash
    print(f'Palavra: "{texto}" -  Hash: {hashRes}')
