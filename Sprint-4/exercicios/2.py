def conta_vogais(texto: str) -> int:
    # Função lambda para verificar se um caractere é uma vogal (sem acentos)
    vogal = lambda char: char.lower() in 'aeiou'
    
    # Filtra os caracteres que são vogais usando a função filter
    vogais = filter(vogal, texto)
    
    # Usa a função len para contar as vogais
    qtdVogais = len(list(vogais))
    
    return qtdVogais