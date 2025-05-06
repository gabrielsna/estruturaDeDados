#include <stdio.h>
#include <stdlib.h>

int posicao, continua;

struct TbFicha {
    int codigo;
    char nome[40];
    char bairro[40];
    char cidade[60];
    char telefone[10];
};

struct TbProduto {
    int codigo;
    char produto[50];
    float valor;
    int quantidade;
};

struct TbFicha ficha[10];     // até 10 clientes
struct TbProduto estoque[10]; // até 10 produtos

void insereCliente() {
    printf("Informe um codigo para o cliente: ");
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

void insereProduto() {
    printf("Informe um codigo para o produto: ");
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

int main() {
    int opcao;

    do {
        printf("Escolha uma opção:\n");
        printf("1 - Inserir Cliente\n");
        printf("2 - Inserir Produto\n");
        printf("3 - Exibir Cliente\n");
        printf("4 - Exibir Produto\n");
        printf("0 - Sair\n");
        scanf("%i", &opcao);

        if (opcao == 1) {
            printf("Informe a posição para guardar o cliente (0 a 9): ");
            scanf("%i", &posicao);
            insereCliente();
        }
        else if (opcao == 2) {
            printf("Informe a posição para guardar o produto (0 a 9): ");
            scanf("%i", &posicao);
            insereProduto();
        }
        else if (opcao == 3) {
            printf("Informe a posição do cliente para exibir (0 a 9): ");
            scanf("%i", &posicao);
            exibeCliente();
        }
        else if (opcao == 4) {
            printf("Informe a posição do produto para exibir (0 a 9): ");
            scanf("%i", &posicao);
            exibeProduto();
        }

        if (opcao != 0) {
            printf("\nDigite 1 para continuar ou 0 para sair: ");
            scanf("%i", &continua);
            system("cls"); // Use "clear" no Linux/Mac
        }
    } while (continua == 1);

    return 0;
}
