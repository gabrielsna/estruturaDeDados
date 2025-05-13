class Cliente:
    def __init__(self, codigo, nome, bairro, cidade, telefone):
        self.codigo = codigo
        self.nome = nome
        self.bairro = bairro
        self.cidade = cidade
        self.telefone = telefone


class Produto:
    def __init__(self, codigo, nome, valor, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade


class VendaItem:
    def __init__(self, codigo_venda, codigo_produto, quantidade, total_item):
        self.codigo_venda = codigo_venda
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade
        self.total_item = total_item


class Venda:
    def __init__(self, codigo, codigo_cliente):
        self.codigo = codigo
        self.codigo_cliente = codigo_cliente
        self.total_itens = 0
        self.total_venda = 0.0


clientes = []
produtos = []
vendas = []
venda_itens = []


def buscar_cliente(codigo):
    for cliente in clientes:
        if cliente.codigo == codigo:
            return cliente
    return None


def buscar_produto(codigo):
    for produto in produtos:
        if produto.codigo == codigo:
            return produto
    return None


def inserir_cliente():
    codigo = int(input("Código do cliente: "))
    nome = input("Nome: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    telefone = input("Telefone: ")
    clientes.append(Cliente(codigo, nome, bairro, cidade, telefone))
    print("Cliente cadastrado.\n")


def inserir_produto():
    codigo = int(input("Código do produto: "))
    nome = input("Nome do produto: ")
    valor = float(input("Valor: "))
    quantidade = int(input("Quantidade em estoque: "))
    produtos.append(Produto(codigo, nome, valor, quantidade))
    print("Produto cadastrado.\n")


def exibir_cliente():
    codigo = int(input("Código do cliente: "))
    cliente = buscar_cliente(codigo)
    if cliente:
        print(f"\nNome: {cliente.nome}")
        print(f"Bairro: {cliente.bairro}")
        print(f"Cidade: {cliente.cidade}")
        print(f"Telefone: {cliente.telefone}\n")
    else:
        print("Cliente não encontrado.\n")


def exibir_produto():
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)
    if produto:
        print(f"\nNome: {produto.nome}")
        print(f"Valor: R$ {produto.valor:.2f}")
        print(f"Quantidade: {produto.quantidade}\n")
    else:
        print("Produto não encontrado.\n")


def realizar_venda():
    codigo_cliente = int(input("Código do cliente: "))
    cliente = buscar_cliente(codigo_cliente)
    if not cliente:
        print("Cliente não encontrado.\n")
        return

    codigo_venda = len(vendas)
    venda = Venda(codigo_venda, codigo_cliente)

    while True:
        codigo_produto = int(input("Código do produto: "))
        produto = buscar_produto(codigo_produto)
        if not produto:
            print("Produto não encontrado.")
            continue

        qtd = int(input("Quantidade: "))
        if qtd > produto.quantidade:
            print("Estoque insuficiente.")
            continue

        subtotal = qtd * produto.valor
        produto.quantidade -= qtd
        venda_itens.append(VendaItem(codigo_venda, codigo_produto, qtd, subtotal))

        venda.total_itens += qtd
        venda.total_venda += subtotal

        cont = input("Adicionar mais produtos? (s/n): ")
        if cont.lower() != 's':
            break

    vendas.append(venda)
    print(f"Venda realizada! Total: R$ {venda.total_venda:.2f}\n")


def exibir_venda():
    codigo = int(input("Código da venda: "))
    if codigo >= len(vendas):
        print("Venda não encontrada.\n")
        return

    venda = vendas[codigo]
    cliente = buscar_cliente(venda.codigo_cliente)

    print(f"\n--- Venda {codigo} ---")
    print(f"Cliente: {cliente.nome}")
    print(f"Total de Itens: {venda.total_itens}")
    print(f"Total da Venda: R$ {venda.total_venda:.2f}\n")


def menu():
    while True:
        print("1 - Inserir Cliente")
        print("2 - Inserir Produto")
        print("3 - Exibir Cliente")
        print("4 - Exibir Produto")
        print("5 - Realizar Venda")
        print("6 - Exibir Venda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_cliente()
        elif opcao == '2':
            inserir_produto()
        elif opcao == '3':
            exibir_cliente()
        elif opcao == '4':
            exibir_produto()
        elif opcao == '5':
            realizar_venda()
        elif opcao == '6':
            exibir_venda()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
