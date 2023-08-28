import json

arquivo = "person.json"
with open(arquivo, 'r') as arquivojson:
    arq = json.load(arquivojson)
    print(arq)