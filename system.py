# Importação do módulo *os* para manipulação de arquivos.
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
        file = open('./orders/order_id%d.txt' % cpf, 'r')
        if file:
            order = file.read().replace('\n', '').split(';')
            if int(order[1]) == cpf:
                file.close()
                return True
    except:
            return False
# Fim da função de verificação de pedido.


# Função responsável por criar um novo pedido.
def createNewOrder():
    print('Criar conta')
    name = input('Nome: ')
    cpf = int(input('CPF (apenas números): '))
    password = input('Senha: ')

    checkOrder = checkOrderExist(cpf)
    if checkOrder:
        print()
        print('Você já possui um pedido em andamento.\nEstamos te redirecionando ao menu de opções.')
        print()
        return

    orderFile = open('./orders/order_id%d.txt' % cpf, 'w')
    orderFile.write('%s;%d;%s;\n' % (name, cpf, password))
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
    orderFile = open('./orders/order_id%d.txt' % cpf, 'a')
    orderFile.write('{0};{1};{2};{3}'.format(code, menu[1][code-1], menu[2][code-1], quantity))
    orderFile.close()
# Fim da função criar pedido.


# Função responsável por cancelar um pedido
def cancelOrder(cpf, pwd):
    try:
        file = open('./orders/order_id%d.txt' % cpf, 'r')
        if file:
            order = file.read().replace('\n', '').split(';')
            if int(order[1]) == cpf and order[2] == pwd:
                file.close()
                os.remove('./orders/order_id%d.txt' % cpf)
                return True
    except ValueError:
        print(ValueError)
        return False

# Fim da função cancelar pedido



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
        confirmation = createNewOrder()

    elif option == 2:
        print('Cancelar pedido')
        cpf = int(input('Digite o CPF (apenas números): '))
        password = input('Digite a senha: ')
        response = cancelOrder(cpf, password)
        if response:
            print('Pedido cancelado com sucesso!')
        else:
            print('CPF ou Senha incorretos.')

    elif option == 0:
        print()
        print('Agredecemos por sua presença. Volte sempre!')
        break


