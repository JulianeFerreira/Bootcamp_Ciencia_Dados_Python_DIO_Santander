ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# Organiza os ativos em ordem alfabética
ativos.sort()

# Imprime os ativos organizados em ordem alfabética
for ativo in ativos:
    print(ativo)
