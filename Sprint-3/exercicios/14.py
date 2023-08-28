def parametros(*naoNomeados, **nomeados):
    for parametro in naoNomeados:
        print(parametro)
    for a, b in nomeados.items():
        print(b)

parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)