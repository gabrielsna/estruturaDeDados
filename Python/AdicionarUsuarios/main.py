import json
import os

ARQUIVO = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

def adicionar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    usuarios = carregar_usuarios()
    usuarios.append({"nome": nome, "email": email})
    salvar_usuarios(usuarios)
    print("Usuário adicionado!")

def listar_usuarios():
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for i, u in enumerate(usuarios):
        print(f"{i + 1}. {u['nome']} - {u['email']}")

def buscar_usuario():
    termo = input("Buscar por nome ou email: ").lower()
    usuarios = carregar_usuarios()
    encontrados = [u for u in usuarios if termo in u['nome'].lower() or termo in u['email'].lower()]
    for u in encontrados:
        print(f"{u['nome']} - {u['email']}")
    if not encontrados:
        print("Nenhum usuário encontrado.")

def remover_usuario():
    listar_usuarios()
    usuarios = carregar_usuarios()
    try:
        indice = int(input("Número do usuário para remover: ")) - 1
        if 0 <= indice < len(usuarios):
            removido = usuarios.pop(indice)
            salvar_usuarios(usuarios)
            print(f"Usuário {removido['nome']} removido.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n1. Adicionar\n2. Listar\n3. Buscar\n4. Remover\n5. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            remover_usuario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
