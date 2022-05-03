# Importação do módulo *os* para manipulação de arquivos.
from math import prod
import os

# Criação de uma matriz 3/7 para o armazenamento dos códigos, produtos e preços.
menu = [
    [1, 2, 3, 4, 5, 6, 7],
    ["X-salada", "X-burger", "Cachorro quente", "Misto quente", "Salada de frutas", "Refrigerante", 
    "Suco natural"],
    [10.00, 10.00, 7.50, 8.00, 5.50, 4.50, 6.25]
]

# Função responsável por verificar se já existe um pedido no CPF cadastrado.
def checkOrderExist(cpf):
    try:
        file = open('./orders/order_id%d.txt' % cpf, 'r', encoding='utf-8')
        if file:
            order = file.read().replace('\n', '').split(';')
            if int(order[1]) == cpf:
                file.close()
                return True
    except:
            return False
# Fim da função de verificação de pedido.


# Função responsável por criar um novo pedido.
def createNewOrder(name, cpf, pwd, addOtherProd):
    checkOrder = False
    if not addOtherProd:
        checkOrder = checkOrderExist(cpf = 0)

    if checkOrder:
        print()
        print('Você já possui um pedido em andamento.\nEstamos te redirecionando ao menu de opções.')
        print()
        return False
    else:
        if not addOtherProd:
            orderFile = open('./orders/order_id%d.txt' % cpf, 'w', encoding='utf-8')
            orderFile.write('%s;%d;%s;\n' % (name, cpf, pwd))
            orderFile.close()

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
        orderFile = open('./orders/order_id%d.txt' % cpf, 'a', encoding='utf-8')
        orderFile.write('{0};{1};{2};{3}\n'.format(code, quantity, menu[1][code-1], menu[2][code-1]))
        orderFile.close()
        return True
# Fim da função criar pedido.

# Função responsável por validar CPF e Senha
def verifyCustomerData(cpf, pwd):
    try:
        file = open('./orders/order_id%d.txt' % cpf, 'r', encoding='utf-8')
        if file:
            order = file.read().replace('\n', '').split(';')
            if int(order[1]) == cpf and order[2] == pwd:
                file.close()
                return True
    except:
        return False
# Fim da função validadora de dados pessoais

# Função responsável por inserir um produto no pedido do cliente
def insertProdIntoOrder(cpf, pwd):
    checkData = verifyCustomerData(cpf, pwd)
    if checkData:
        response = createNewOrder('', cpf, '', True)
        return response
    else:
        return False

# Fim da função inserir produto

# Função responsável por cancelar um produto no pedido do cliente
def cancelProduct(cpf, pwd, code, quant):
    checkData = verifyCustomerData(cpf, pwd)
    if checkData:
        orderFile = open('./orders/order_id%d.txt' % cpf, 'r', encoding='utf-8')
        data = orderFile.read().replace('\n', '').split(';')
        personalData = [data[0], data[1], data[2]]
        products = data[3:]
        print(products)
    else:
        return False
# Fim da função cancelar produto no pedido

print()

#Loop infinito para apresentar o menu de opções.
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
        print()
        print('---- Criar conta ----')
        print()

        name = input('Nome: ')
        cpf = int(input('CPF (apenas números): '))
        password = input('Senha: ')
        print()
        confirmation = createNewOrder(name, cpf, password, False)

        if confirmation:
            print()
            print('Pedido criado com sucesso!')
            print()
            otherProduct = input('Deseje adicionar outro produto? (s/n): ')
            if otherProduct == 's':
                createNewOrder('', cpf, '', True)

    elif option == 2:
        print()
        print('---- Cancelar pedido ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        response = verifyCustomerData(cpf, password)

        if response:
            os.remove('./orders/order_id%d.txt' % cpf)
            print('Pedido cancelado com sucesso!')
            print()
        else:
            print('CPF ou Senha incorretos.')
            print()

    elif option == 3:
        print()
        print('---- Inserir produto no pedido ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        print()
        response = insertProdIntoOrder(cpf, password)

        if response:
            print()
            print('Seu produto foi inserido no pedido.')
            print()
        else:
            print()
            print('CPF ou Senha inválidos.')
            print()

    elif option == 4:
        print()
        print('---- Cancelar produto no pedido ----')
        print()

        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        print()
        cancelProduct(cpf, password, 0, 0)

    elif option == 0:
        print()
        print('Agredecemos por sua presença. Volte sempre!')
        break


