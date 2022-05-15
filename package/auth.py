# Módulo criado para a realização de autenticações.

# Função responsável por verificar se já existe um pedido no CPF informado pelo usuário.
def checkOrderExist(cpf):
    try:
        # Abertura do arquivo de dados do cliente.
        file = open('./customer/user%d.txt' % cpf, 'r', encoding='utf-8')
        if file:
            order = file.read().split(';')
            if int(order[1]) == cpf:
                file.close()
                return True
    except:
            return False
# Fim da função de verificação de pedido.

# Função responsável por validar CPF e Senha do usuário.
def verifyCustomerData(cpf, pwd):
    try:
        file = open('./customer/user%d.txt' % cpf, 'r', encoding='utf-8')
        if file:
            data = file.read().split(';')
            file.close()
            if int(data[1]) == cpf and data[2] == pwd:
                return True
            else:
                return False
    except:
        return False
# Fim da função validadora de dados pessoais