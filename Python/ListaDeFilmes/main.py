import requests
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import io

# Substitua com sua API key do OMDb
API_KEY = "97cc7390"

def buscar_filme():
    titulo = entrada_titulo.get()
    if not titulo:
        messagebox.showwarning("Atenção", "Digite o nome de um filme!")
        return

    url = f"http://www.omdbapi.com/?t={titulo}&apikey={API_KEY}&language=pt-BR"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        messagebox.showerror("Erro", "Falha ao conectar à API.")
        return

    dados = resposta.json()

    if dados.get('Response') == 'False':
        messagebox.showinfo("Não encontrado", "Filme não encontrado.")
        return

    # Preenche os dados
    resultado_var.set(
        f"Título: {dados.get('Title')}\n"
        f"Ano: {dados.get('Year')}\n"
        f"Gênero: {dados.get('Genre')}\n"
        f"Diretor: {dados.get('Director')}\n"
        f"Atores: {dados.get('Actors')}\n"
        f"Nota IMDb: {dados.get('imdbRating')}\n"
        f"Idioma: {dados.get('Language')}\n"
        f"País: {dados.get('Country')}\n"
        f"\nSinopse:\n{dados.get('Plot')}"
    )

    # Exibe imagem do pôster
    poster_url = dados.get('Poster')
    if poster_url and poster_url != "N/A":
        imagem_resposta = requests.get(poster_url)
        imagem = Image.open(io.BytesIO(imagem_resposta.content))
        imagem = imagem.resize((200, 300))
        imagem_tk = ImageTk.PhotoImage(imagem)
        poster_label.config(image=imagem_tk)
        poster_label.image = imagem_tk
    else:
        poster_label.config(image="", text="Sem imagem disponível")

# Criando a janela
janela = tk.Tk()
janela.title("Consulta de Filmes")
janela.geometry("600x700")

# Entrada
tk.Label(janela, text="Digite o nome do filme:").pack(pady=5)
entrada_titulo = tk.Entry(janela, width=40)
entrada_titulo.pack()

# Botão de busca
tk.Button(janela, text="Buscar", command=buscar_filme).pack(pady=10)

# Resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado_var, justify="left", wraplength=550)
resultado_label.pack(pady=10)

# Imagem do pôster
poster_label = tk.Label(janela)
poster_label.pack(pady=10)

# Inicia a interface
janela.mainloop()
