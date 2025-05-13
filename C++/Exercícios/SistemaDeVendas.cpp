#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CLIENTES 10
#define MAX_PRODUTOS 10
#define MAX_VENDAS 10
#define MAX_ITENS_POR_VENDA 20

int posicao, continua;

struct TbFicha {
    int codigo;
    char nome[40];
    char bairro[40];
    char cidade[60];
    char telefone[15];
};

struct TbProduto {
    int codigo;
    char produto[50];
    float valor;
    int quantidade;
};

struct TbVenda {
    int codigo;
    int codigoCliente;
    int totalItens;
    float totalVenda;
};

struct TbVendaItem {
    int codigoVenda;
    int codigoProduto;
    int quantidade;
    float totalItem;
};

struct TbFicha ficha[MAX_CLIENTES];
struct TbProduto estoque[MAX_PRODUTOS];
struct TbVenda vendas[MAX_VENDAS];
struct TbVendaItem vendaItens[MAX_VENDAS * MAX_ITENS_POR_VENDA];

int totalVendas = 0;
int totalItens = 0;

// ============================== Funções auxiliares

int buscaCliente(int cod) {
    for (int i = 0; i < MAX_CLIENTES; i++) {
        if (ficha[i].codigo == cod) return i;
    }
    return -1;
}

int buscaProduto(int cod) {
    for (int i = 0; i < MAX_PRODUTOS; i++) {
        if (estoque[i].codigo == cod) return i;
    }
    return -1;
}

// ============================== Funções de cliente

void insereCliente() {
    printf("Informe um código para o cliente: ");
    scanf("%i", &ficha[posicao].codigo);
    printf("Informe o nome do cliente: ");
    scanf("%s", ficha[posicao].nome);
    printf("Informe o bairro do cliente: ");
    scanf("%s", ficha[posicao].bairro);
    printf("Informe a cidade do cliente: ");
    scanf("%s", ficha[posicao].cidade);
    printf("Informe o telefone: ");
    scanf("%s", ficha[posicao].telefone);
}

void exibeCliente() {
    printf("\nInformações do cliente:\n");
    printf("Código: %i\n", ficha[posicao].codigo);
    printf("Nome: %s\n", ficha[posicao].nome);
    printf("Bairro: %s\n", ficha[posicao].bairro);
    printf("Cidade: %s\n", ficha[posicao].cidade);
    printf("Telefone: %s\n", ficha[posicao].telefone);
}

// ============================== Funções de produto

void insereProduto() {
    printf("Informe um código para o produto: ");
    scanf("%i", &estoque[posicao].codigo);
    printf("Informe o nome do produto: ");
    scanf("%s", estoque[posicao].produto);
    printf("Informe o valor do produto: ");
    scanf("%f", &estoque[posicao].valor);
    printf("Informe a quantidade em estoque: ");
    scanf("%i", &estoque[posicao].quantidade);
}

void exibeProduto() {
    printf("\nInformações do produto:\n");
    printf("Código: %i\n", estoque[posicao].codigo);
    printf("Produto: %s\n", estoque[posicao].produto);
    printf("Valor: R$ %.2f\n", estoque[posicao].valor);
    printf("Quantidade: %i\n", estoque[posicao].quantidade);
}

// ============================== Funções de venda

void realizaVenda() {
    int codCliente, codProduto, qtdProduto, indexCliente, indexProduto;
    float total = 0.0;
    int itensNaVenda = 0;

    printf("Código do cliente: ");
    scanf("%d", &codCliente);

    indexCliente = buscaCliente(codCliente);
    if (indexCliente == -1) {
        printf("Cliente não encontrado.\n");
        return;
    }

    int codVenda = totalVendas;
    vendas[codVenda].codigo = codVenda;
    vendas[codVenda].codigoCliente = codCliente;
    vendas[codVenda].totalItens = 0;
    vendas[codVenda].totalVenda = 0.0;

    char continuar;
    do {
        printf("Código do produto: ");
        scanf("%d", &codProduto);
        indexProduto = buscaProduto(codProduto);
        if (indexProduto == -1) {
            printf("Produto não encontrado.\n");
        } else {
            printf("Quantidade desejada: ");
            scanf("%d", &qtdProduto);
            if (qtdProduto <= estoque[indexProduto].quantidade) {
                float subtotal = estoque[indexProduto].valor * qtdProduto;
                estoque[indexProduto].quantidade -= qtdProduto;

                vendaItens[totalItens].codigoVenda = codVenda;
                vendaItens[totalItens].codigoProduto = codProduto;
                vendaItens[totalItens].quantidade = qtdProduto;
                vendaItens[totalItens].totalItem = subtotal;
                totalItens++;

                total += subtotal;
                itensNaVenda += qtdProduto;

                printf("Produto adicionado!\n");
            } else {
                printf("Estoque insuficiente.\n");
            }
        }

        printf("Adicionar outro produto? (s/n): ");
        scanf(" %c", &continuar);
    } while (continuar == 's' || continuar == 'S');

    vendas[codVenda].totalItens = itensNaVenda;
    vendas[codVenda].totalVenda = total;
    totalVendas++;

    printf("Venda realizada com sucesso! Total: R$ %.2f\n", total);
}

void exibeVenda() {
    int codVenda;
    printf("Digite o código da venda: ");
    scanf("%d", &codVenda);

    if (codVenda >= totalVendas) {
        printf("Venda não encontrada.\n");
        return;
    }

    int clienteIndex = buscaCliente(vendas[codVenda].codigoCliente);
    if (clienteIndex == -1) {
        printf("Cliente da venda não encontrado.\n");
        return;
    }

    printf("\n--- Venda %d ---\n", codVenda);
    printf("Cliente: %s\n", ficha[clienteIndex].nome);
    printf("Total de itens: %d\n", vendas[codVenda].totalItens);
    printf("Valor total: R$ %.2f\n", vendas[codVenda].totalVenda);
}

// ============================== Menu principal

int main() {
    int opcao;

    do {
        printf("Escolha uma opção:\n");
        printf("1 - Inserir Cliente\n");
        printf("2 - Inserir Produto\n");
        printf("3 - Exibir Cliente\n");
        printf("4 - Exibir Produto\n");
        printf("5 - Realizar Venda\n");
        printf("6 - Exibir Venda\n");
        printf("0 - Sair\n");
        scanf("%i", &opcao);

        switch (opcao) {
            case 1:
                printf("Informe a posição para guardar o cliente (0 a 9): ");
                scanf("%i", &posicao);
                insereCliente();
                break;
            case 2:
                printf("Informe a posição para guardar o produto (0 a 9): ");
                scanf("%i", &posicao);
                insereProduto();
                break;
            case 3:
                printf("Informe a posição do cliente para exibir (0 a 9): ");
                scanf("%i", &posicao);
                exibeCliente();
                break;
            case 4:
                printf("Informe a posição do produto para exibir (0 a 9): ");
                scanf("%i", &posicao);
                exibeProduto();
                break;
            case 5:
                realizaVenda();
                break;
            case 6:
                exibeVenda();
                break;
        }

        if (opcao != 0) {
            printf("\nDigite 1 para continuar ou 0 para sair: ");
            scanf("%i", &continua);
            system("cls"); // Use "clear" no Linux/Mac
        }

    } while (continua == 1);

    return 0;
}
