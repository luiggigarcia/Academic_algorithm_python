import datetime
# Esse módulo possui as funções de Valor do pedido e Extrado do pedido.

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