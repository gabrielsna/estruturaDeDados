import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa():
    titulo = input("Título da tarefa: ")
    tarefas = carregar_tarefas()
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada.")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, t in enumerate(tarefas):
        status = "✅" if t["concluida"] else "❌"
        print(f"{i + 1}. {t['titulo']} [{status}]")

def marcar_concluida():
    listar_tarefas()
    tarefas = carregar_tarefas()
    try:
        idx = int(input("Número da tarefa para marcar como concluída: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefas[idx]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_tarefa():
    listar_tarefas()
    tarefas = carregar_tarefas()
    try:
        idx = int(input("Número da tarefa para remover: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefa = tarefas.pop(idx)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{tarefa['titulo']}' removida.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar como concluída\n4. Remover tarefa\n5. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
