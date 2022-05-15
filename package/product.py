from package.auth import checkOrderExist

# Módulo relacionado as funções de inserção, deleção e alteração do pedido.

# Função responsável por criar um novo pedido.
def createNewOrder(name, cpf, pwd, newProduct):
    # Criação de uma matriz 3 linhas / 7 colunas para o armazenamento dos códigos, produtos e preços.
    menu = [
        [1, 2, 3, 4, 5, 6, 7],
        ["X-salada", "X-burger", "Cachorro quente", "Misto quente", "Salada de frutas", "Refrigerante", 
         "Suco natural"],
        [10.00, 10.00, 7.50, 8.00, 5.50, 4.50, 6.25]
]
    # A variável 'checkOrder' indica se já existe um pedido no CPF informado.
    checkOrder = False
    # O parâmetro 'newProduct' indica se cliente deseja inserir um produto em seu pedido.
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

        # Criação de uma estrutura de repetição para mostrar as opções de pedido.
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
   
    # A variável 'prodQuant' armazena a quantidade existente de produtos no pedido.
    prodQuant = 0
    for prod in products:
        if code == int(prod[0]) and 'cancelado' not in prod:
            prodQuant += 1

    if quant <= prodQuant:
        for i in range(quant):
            for prod in products:
                if int(prod[0]) == code and 'cancelado' not in prod:
                    prod.append('cancelado')
                    break
       
        file = open('./orders/order_id%d.txt' % (cpf), 'w', encoding='utf-8')
        for i in range(len(products)):
                # Essa condição avalia se é o ultimo produto a ser escrito no arquivo,
                # Assim, não é colocado uma quebra de linha.
                if i == len(products)-1:
                    file.write(';'.join(products[i]))
                else:
                    file.write('{0}\n'.format(';'.join(products[i])))
        file.close()
        return True
    else:
        return False
# Fim da função cancelar produto no pedido