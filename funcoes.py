def informacoes(resposta):
    print("Digite as informações solicitadas")

    nome_pagador = input("Digite o nome do Pagador: ")
    nome_pagador = nome_pagador.upper()
    valor = input("Digite o Valor númerico (Ex.: XXX,XX): ")
    valor_extenso = input("Digite o Valor por extenso: ")
    valor_extenso = valor_extenso.lower()
    cpf = input("Digite o CPF do pagador (Sem os pontos): ")
    while True:
        if len(cpf) != 11 :
            print("CPF inválido, digite novamente")
            cpf = input("Digite o CPF do pagador (Sem os pontos): ")
        else:
            break
    cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    rg = input("Digite o RG do Pagador: ")
    orgao = input("Digite orgão emissor do RG: ")
    telefone = input("Digite o número de telefone: ")
    if resposta == "1":
        anos_aberto = input("Digite os anos em aberto (Ex.: 2021 a 2025): ")
    endereco = input("Digite o endereço: ")
    cadastro = input("Digite o cadastro imobiliário: ")
    inscricao = input("Digite inscrição imobiliária: ")
    area_terreno = input("Digite a área do terreno: ")
    codigo_cadastro = int(input("Digite o Código de cadastro que está presente no Théos: "))
    patrimonio = input("Digite o Patrimônio Foreiro: ")
    patrimonio = patrimonio.upper()
    numero_boleto = int(input("Digite o número do boleto: "))
    vencimento_boleto = input("Digite a data de vencimento do boleto (XX/XX/XXXX): ")
    data_pagamento = input("Digite a data de Pagamento (XX/XX/XXXX): ")

    if resposta == '1':
        return nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, anos_aberto, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento
    else:
        return nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento
    

def texto_foro(nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, anos_aberto, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento):
    print(f"Recebi do(a) Sr(a). {nome_pagador}, portador(a) do RG nº {rg} {orgao}, inscrito(a) no CPF sob nº {cpf}, telefone: {telefone}, a importância de R$ {valor}({valor_extenso}), referente ao foro de {anos_aberto} do domínio útil do terreno localizado na {endereco}, cadastro imobiliário: {cadastro}, inscrição imobiliária: {inscricao}, área do terreno: {area_terreno}, cadastrado no código nº {codigo_cadastro}, foreiro ao patrimônio de {patrimonio}. A quitação foi realizada via boleto bancário de nº {numero_boleto}, através da conta de nº 159-7/71875-0, com vencimento para o dia {vencimento_boleto}, pago no dia {data_pagamento}.")

    timeout = input("Aperte Enter para continuar")

def texto_laudemio(nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento):
    print(f"Recebi do(a) Sr(a). {nome_pagador}, portador(a) do RG nº {rg} {orgao}, inscrito(a) no CPF sob nº {cpf}, telefone: {telefone}, a importância de R$ {valor}({valor_extenso}), referente ao Laudêmio de Transferência do domínio útil do terreno localizado na {endereco}, cadastro imobiliário: {cadastro}, inscrição imobiliária: {inscricao}, área do terreno: {area_terreno}, cadastrado no código nº {codigo_cadastro}, foreiro ao patrimônio de {patrimonio}. A quitação foi realizada via boleto bancário de nº {numero_boleto}, através da conta de nº 159-7/71875-0, com vencimento para o dia {vencimento_boleto}, pago no dia {data_pagamento}. Por esse ato se efetua a transferência do Domínio Útil do terreno que antes pertencia a XXXXXX, inscrito no CPF sob nº XXX.XXX.XXX-XX, passando a pertencer titularidade para {nome_pagador}.")

    timeout = input("Aperte Enter para continuar")

def texto_dominio():
    print("")