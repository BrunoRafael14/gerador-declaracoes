from funcoes import informacoes, texto_foro, texto_laudemio, texto_dominio

print("Bem vindo, Escolha uma opção: \n1- Foro \n2- Laudêmio\n3- Domínio Direto")

resposta = input("")

if resposta == '1':
    nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, anos_aberto, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento = informacoes(resposta)
else:
    nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento = informacoes(resposta)

if resposta == '1':
    modelo = texto_foro(nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, anos_aberto, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento)

elif resposta == '2':
    modelo = texto_laudemio(nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento)

elif resposta == '3':
    modelo = texto_dominio(nome_pagador, valor, valor_extenso, cpf, rg, orgao, telefone, endereco, cadastro, inscricao, area_terreno, codigo_cadastro, patrimonio, numero_boleto, vencimento_boleto, data_pagamento)

