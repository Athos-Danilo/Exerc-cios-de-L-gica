def processar_produtos(produtos):
    total_quantidades = {}
    total_valor = 0
    total_itens = 0
    
    for produto in produtos:
        nome = produto['nome']
        valor = produto['valor']
        quantidade = produto['quantidade']
        
        if nome in total_quantidades:
            total_quantidades[nome] += quantidade
        else:
            total_quantidades[nome] = quantidade
        
        total_valor += valor * quantidade
        total_itens += quantidade
    
    if total_itens > 0:
        valor_medio = total_valor / total_itens
    else:
        valor_medio = 0
    
    return {"quantidades": total_quantidades, "valor_medio": valor_medio}

# Exemplo de uso
produtos = [
    {'nome': 'Feijão', 'valor': 5.3, 'quantidade': 3},
    {'nome': 'Arroz', 'valor': 3.2, 'quantidade': 2},
    {'nome': 'Feijão', 'valor': 5.3, 'quantidade': 5},
    {'nome': 'Macarrão', 'valor': 2.5, 'quantidade': 1},
    {'nome': 'Arroz', 'valor': 3.2, 'quantidade': 4},
    {'nome': 'Feijão', 'valor': 5.3, 'quantidade': 2}
]

resultado = processar_produtos(produtos)
print(resultado)