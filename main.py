# Importação dos módulos de produto, autenticação e extrato do pedido.
from package.product import createNewOrder, cancelProduct, insertProdIntoOrder
from package.auth import verifyCustomerData
from package.statement import valueToPay, getOrderStatement
# Importação do módulo "os" para manipulação de arquivos.
import os

print()

if __name__ == '__main__':
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
                    response = createNewOrder('', cpf, '', True)
                    if response:
                        print('O produto inserido no pedido.')

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
            if  validation:
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
                if response or response == 0:
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


