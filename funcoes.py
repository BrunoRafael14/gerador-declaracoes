def informacoes(resposta):
    print("Digite as informações solicitadas")

    nome_pagador = input("Digite o nome do Pagador ")
    valor = input("Digite o Valor númerico ")
    valor_extenso = input("Digite o Valor por extenso ")
    cpf = input("Digite o CPF do pagador (Sem os pontos) ")
    rg = input("Digite o RG do Pagador (Sem os pontos) ")
    orgao = input("Digite orgão emissor do RG ")
    telefone = input("Digite o número de telefone (Apenas números, sem espaços) ")
    if resposta == 1:
        anos_aberto = input("Digite os anos em aberto (Ex.: 2021 a 2025) ")
    endereco = input("Digite o endereço")
    cadastro = input("Digite o cadastro imobiliário (apenas números) ")
    inscricao = input("Digite inscrição imobiliária (apenas números) ")
    area_terreno = float(input("Digite a área do terreno (Apenas numeros e virgula se for decimal) "))
    codigo_cadastro = int(input("Digite o Código de cadastro que está presente no Théos "))
    patrimonio = input("Digite o Patrimônio Foreiro ")
    numero_boleto = int(input("Digite o número do boleto "))
    vencimento_boleto = input("Digite a data de vencimento do boleto ")
    data_pagamento = input("Digite a data de Pagamento ")

    if resposta == '1':
        return nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, anos_aberto, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento
    else:
        return nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento