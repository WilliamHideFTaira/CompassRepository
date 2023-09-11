def calcular_valor_maximo(operadores, operandos) -> float:
    # Função para aplicar operações a pares de operandos
    def operacao(operador, operandos):
        if operador == '+':
            return operandos[0] + operandos[1]
        elif operador == '-':
            return operandos[0] - operandos[1]
        elif operador == '*':
            return operandos[0] * operandos[1]
        elif operador == '/':
            return operandos[0] / operandos[1]
        elif operador == '%':
            return operandos[0] % operandos[1]
    
    # Combinar operadores e operandos na ordem correta
    operacoes = list(zip(operadores, operandos))
    
    # Aplicar operações a cada par de operandos
    resultados = list(map(lambda x: operacao(x[0], x[1]), operacoes))
    
    # Encontrar o maior valor entre os resultados
    maximo = max(resultados)
    
    return maximo