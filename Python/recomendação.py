# Dados fictícios para demonstração
dados_acoes = {
    'PETR4.SA': {'LPA': 10.5, 'P/L': 8.2, 'ROE': 0.12},
    'VALE3.SA': {'LPA': 6.8, 'P/L': 12.1, 'ROE': 0.08},
    'BBAS3.SA': {'LPA': 3.2, 'P/L': 15.5, 'ROE': 0.09},
    # Insira mais dados para outras ações aqui
}

# Função para calcular a margem de segurança
def calcular_margem_seguranca(acao):
    lpa = dados_acoes[acao]['LPA']
    p_l = dados_acoes[acao]['P/L']
    roe = dados_acoes[acao]['ROE']
    margem_seguranca = (lpa * roe * 7.5) / p_l
    return margem_seguranca

# Função para listar as melhores ações
def listar_melhores_acoes(n):
    acoes = list(dados_acoes.keys())
    melhores_acoes = []
    
    # Calcular a margem de segurança para cada ação e armazenar em uma lista
    for acao in acoes:
        margem_seguranca = calcular_margem_seguranca(acao)
        melhores_acoes.append({'Ação': acao, 'Margem de Segurança': margem_seguranca})
    
    # Ordenar a lista de ações pela margem de segurança em ordem decrescente
    melhores_acoes = sorted(melhores_acoes, key=lambda x: x['Margem de Segurança'], reverse=True)
    
    # Retornar as top n ações com base na margem de segurança
    return melhores_acoes[:n]

# Utilize a função listar_melhores_acoes para obter as 20 melhores ações
melhores_acoes = listar_melhores_acoes(20)
print(melhores_acoes)
