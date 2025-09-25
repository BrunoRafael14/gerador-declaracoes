def informacoes(resposta):
    print("Digite as informações solicitadas")

    nome_pagador = input("Digite o nome do Pagador ")
    valor = input("Digite o Valor númerico ")
    valor_extenso = input("Digite o Valor por extenso ")
    cpf = input("Digite o CPF do pagador (Sem os pontos) ")
    rg = input("Digite o RG do Pagador (Sem os pontos) ")
    orgao = input("Digite orgão emissor do RG ")
    telefone = input("Digite o número de telefone (Apenas números, sem espaços) ")
    if resposta == "1":
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
    

def texto_foro(nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, anos_aberto, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento):
    print(f"Recebi do(a) Sr(a). {nome_pagador}, portador(a) do RG nº {rg} {orgao}, inscrito(a) no CPF sob nº {cpf}, telefone: {telefone}, a importância de R$ {valor}({valor_extenso}), referente ao foro de {anos_aberto} do domínio útil do terreno localizado na {endereco}, cadastro imobiliário: {cadastro}, inscrição imobiliária: {inscricao}, área do terreno: {area_terreno}, cadastrado no código nº {codigo_cadastro}, foreiro ao patrimônio de {patrimonio}. A quitação foi realidaza via boleto bancário de nº {numero_boleto}, através da conta de nº 159-7/71875-0, com vencimento para o dia {vencimento_boleto}, pago no dia {data_pagamento}")

    timeout = input("Aperte Enter para continuar")

def texto_laudemio(nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento):
    print(f"Recebi do(a) Sr(a). {nome_pagador}, portador(a) do RG nº {rg} {orgao}, inscrito(a) no CPF sob nº {cpf}, telefone: {telefone}, a importância de R$ {valor}({valor_extenso}), referente ao Laudêmio de Transferência do domínio útil do terreno localizado na {endereco}, cadastro imobiliário: {cadastro}, inscrição imobiliária: {inscricao}, área do terreno: {area_terreno}, cadastrado no código nº {codigo_cadastro}, foreiro ao patrimônio de {patrimonio}. A quitação foi realidaza via boleto bancário de nº {numero_boleto}, através da conta de nº 159-7/71875-0, com vencimento para o dia {vencimento_boleto}, pago no dia {data_pagamento}. Por esse ato se efetua a transferência do Domínio Útil do terreno que antes pertencia a XXXXXX, inscrito no CPF sob nº XXX.XXX.XXX-XX, passando a pertencer titularidade para {nome_pagador}")

    timeout = input("Aperte Enter para continuar")

def texto_dominio():
    print("")