# Importação do módulo "os" para manipulação de arquivos.
import os
import datetime

# Criação de uma matriz 3 linhas / 7 colunas para o armazenamento dos códigos, produtos e preços.
menu = [
    [1, 2, 3, 4, 5, 6, 7],
    ["X-salada", "X-burger", "Cachorro quente", "Misto quente", "Salada de frutas", "Refrigerante", 
    "Suco natural"],
    [10.00, 10.00, 7.50, 8.00, 5.50, 4.50, 6.25]
]

# Função responsável por verificar se já existe um pedido no CPF informado.
def checkOrderExist(cpf):
    try:
        file = open('./customer/user%d.txt' % cpf, 'r', encoding='utf-8')
        if file:
            order = file.read().split(';')
            if int(order[1]) == cpf:
                file.close()
                return True
    except:
            return False
# Fim da função de verificação de pedido.


# Função responsável por criar um novo pedido.
def createNewOrder(name, cpf, pwd, newProduct):
    checkOrder = False
    if not newProduct:
        checkOrder = checkOrderExist(cpf)

    if checkOrder:
        print()
        print('Você já possui um pedido em andamento.\nEstamos te redirecionando ao menu de opções.')
        print()
        return False
    else:
        if not newProduct:
            register_client = open('./customer/user%d.txt' % cpf, 'w', encoding='utf-8')
            register_client.write('%s;%d;%s' % (name, cpf, pwd))
            register_client.close()
            
        print("{:20}".format("Código"), end=" ")
        print("{:20}".format("Produto"), end=" ")
        print("{:20}".format("Preço"), end=" ")
        print()

        for column in range(len(menu[0])):
            for line in range(len(menu)):
                print("{:20}".format(str(menu[line][column])), end=" ")
            print()
        print()
        code = int(input('Digite o código do produto escolhido: '))
        quantity = int(input('Quantidade: '))
        print()
        order = open('./orders/order_id%d.txt' % cpf, 'a', encoding='utf-8')
        if newProduct:
            order.write('\n{0};{1};{2};{3}'.format(code, quantity, menu[1][code-1], menu[2][code-1]))
        else:
            order.write('{0};{1};{2};{3}'.format(code, quantity, menu[1][code-1], menu[2][code-1]))
            order.close()
            return True
# Fim da função criar pedido.

# Função responsável por validar CPF e Senha do usuário.
def verifyCustomerData(cpf, pwd):
    try:
        file = open('./customer/user%d.txt' % cpf, 'r', encoding='utf-8')
        if file:
            data = file.read().split(';')
            if int(data[1]) == cpf and data[2] == pwd:
                file.close()
                return True
    except:
        return False
# Fim da função validadora de dados pessoais

# Função responsável por inserir um produto no pedido do cliente.
def insertProdIntoOrder(cpf):
    createNewOrder('', cpf, '', True)
    return True
# Fim da função inserir produto

# Função responsável por cancelar um produto no pedido do cliente
def cancelProduct(code, quant, cpf):
    file = open('./orders/order_id%d.txt' % cpf, 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    products = []
    for prod in data:
        products.append(prod.replace('\n','').split(';'))
   
    prodQuant = 0
    for prod in products:
        if code == int(prod[0]) and 'cancelado' not in prod:
            prodQuant += 1

    if quant <= prodQuant:
        if quant == 1:
            quant += 1
        for i in range(quant-1):
            for prod in products:
                if int(prod[0]) == code and 'cancelado' not in prod:
                    prod.append('cancelado')
       
        file = open('./orders/order_id%d.txt' % (cpf), 'w', encoding='utf-8')
        for i in range(len(products)):
                if i == len(products)-1:
                    file.write(';'.join(products[i]))
                else:
                    file.write('{0}\n'.format(';'.join(products[i])))
        file.close()
        return True
    else:
        return False
# Fim da função cancelar produto no pedido

# Função responsável por obter o valor total do pedido.

def valueToPay(cpf):
    file = open('./orders/order_id%d.txt' % cpf, 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    products = []

    for prod in data:
        products.append(prod.replace('\n','').split(';'))

    total = 0
    for prod in products:
        if 'cancelado' not in prod:
            total += float(prod[3])
    return total

# Fim da função valor total.

# Função responsável por gerar o extrato do pedido.
# Inclui o histórico de todas as operações realizadas.
def getOrderStatement(cpf):
    file = open('./customer/user{0}.txt'.format(cpf), 'r', encoding='utf-8')
    data = file.read().split(';')
    file.close()
    statement = '''Nome: {0}
CPF: {1}
Total: R$ {2}
Data: {3}
Itens do pedido: \n'''.format(data[0], data[1], valueToPay(cpf), datetime.datetime.now())

    file = open('./orders/order_id%d.txt' % cpf, 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    products = []
    for prod in data:
        products.append(prod.replace('\n','').split(';'))
    
    items = []
    for prod in products:
        if 'cancelado' in prod:
            items.append([ prod[1], prod[2], prod[3], (float(prod[3])*int(prod[1])), prod[4] ])
        else:
            items.append([ prod[1], prod[2], prod[3], (float(prod[3])*int(prod[1])) ])

    for item in items:
        if 'cancelado' in item:
            statement += '{:2}  -  {:20} - Preço unitário:  {:20}   Valor:  - {:5} - {:5}\n'.format(item[0], item[1], item[2], item[3], item[4].capitalize())
        else:
            statement += '{:2}  -  {:20} - Preço unitário:  {:20}   Valor:  + {:5}\n'.format(item[0], item[1], item[2], item[3])

    return statement

# Fim da função extrato do pedido.

print()

#Estrutura de repetição recursiva para a apresentação do menu de opções.
while True:
    # Variável responsável por armazenar a opção escolhida.
    option = int(input('''1 - Novo Pedido
2 - Cancela Pedido
3 - Insere produto
4 - Cancela produto
5 - Valor do pedido
6 - Extrato do pedido

0 - Sair

Opção desejada: '''))

    print()

    # Inicio das estruturas condicionais para validação e efetivação das opções.
    if option == 1:
        # Opção 01 para criação do pedido
        print()
        print('---- Criar conta ----')
        print()

        name = input('Nome: ')
        cpf = int(input('CPF (apenas números): '))
        password = input('Senha: ')
        print()
        # o 4° parametro da função "createNewOrder" indica a inserção de mais um produto no pedido.
        confirmation = createNewOrder(name, cpf, password, False)

        if confirmation:
            print()
            print('Pedido criado com sucesso!')
            print()
            otherProduct = input('Deseje adicionar outro produto? (s/n): ')
            if otherProduct == 's':
                createNewOrder('', cpf, '', True)

    elif option == 2:
        # Opção 02 para o cancelamento do pedido.
        print()
        print('---- Cancelar pedido ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        response = verifyCustomerData(cpf, password)

        if response:
            os.remove('./orders/order_id%d.txt' % cpf)
            os.remove('./customer/user%d.txt' % cpf)
            print()
            print('Pedido cancelado com sucesso!')
            print()
        else:
            print()
            print('CPF ou Senha incorretos')
            print()

    elif option == 3:
        # Opção 03 para a inserção de um produto no pedido.
        print()
        print('---- Inserir produto no pedido ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        print()
        validation = verifyCustomerData(cpf, password)
        if validation:
            response = insertProdIntoOrder(cpf)
            if response:
                print()
                print('O produto foi inserido em seu pedido.')
                print()
        else:
            print()
            print('CPF ou Senha inválidos.')
            print()

    elif option == 4:
        # Opção 04 para cancelar um produto no pedido.
        print()
        print('---- Cancelar produto no pedido ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        print()
        validation = verifyCustomerData(cpf, password)
        if validation:
            code = int(input('Digite o código do produto: '))
            quant = int(input('Digite a quantidade a ser cancelada: '))
            response = cancelProduct(code, quant, cpf)
            if response:
                print()
                print('O produto foi cancelado em seu pedido!')
                print()
            else:
                print()
                print('Código ou Quantidade de produto inválido')
                print()
        else:
            print()
            print('CPF ou Senha inválidos.')
            print()

    elif option == 5:
        # Opção 04 para obter o valor total do pedido.
        print()
        print('---- Valor a pagar ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        print()
        validation = verifyCustomerData(cpf, password)

        if validation:
            response = valueToPay(cpf)
            if response:
                print()
                print('Valor total: R$ {0}'.format(response))
                print()
        else:
            print()
            print('CPF ou Senha inválidos.')
            print()

    elif option == 6:
        # Opção 06 para obter o extrato do pedido.
        print()
        print('---- Extrato do pedido ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        print()
        validation = verifyCustomerData(cpf, password)

        if validation:
            response = getOrderStatement(cpf)
            if response:
                print()
                print(response)
                print()
        else:
            print()
            print('CPF ou Senha inválidos.')
            print()

    elif option == 0:
        print()
        print('Agredecemos por sua presença. Volte sempre!')
        break


