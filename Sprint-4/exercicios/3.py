from functools import reduce

def calcula_saldo(lancamentos) -> float:
    # Função lambda para calcular o saldo parcial
    parcial = lambda saldo, lancamento: saldo + lancamento[0] if lancamento[1] == 'C' else saldo - lancamento[0]
    
    # Função map para aplicar a função lambda aos lançamentos e obter uma lista de saldos parciais
    saldoParcial = list(map(lambda lancamento: parcial(0.0, lancamento), lancamentos))
    
    # Função reduce para calcular o saldo final a partir dos saldos parciais
    saldoFinal = reduce(lambda x, y: x + y, saldoParcial)
    
    return saldoFinal