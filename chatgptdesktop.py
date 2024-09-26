import json
from tkinter import *
from openai import OpenAI

# Carrega a chave da API a partir de um arquivo JSON
with open("config.json", "r") as file:
    config = json.load(file)
api_key = config['api_key']

client = OpenAI(api_key=api_key)

def obter_resposta():
    pergunta = entrada_usuario.get("1.0", END).strip()  # Lê o texto do campo de entrada
    if not pergunta:
        return  # Não faz nada se o campo de entrada estiver vazio

    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pergunta}],
            max_tokens=150
        )
        
        respostas.append(f"Pergunta: {pergunta}")
        respostas.append(f"Resposta: {resposta.choices[0].message.content}")
        
        lista_perguntas.insert(END, pergunta)
        exibir_respostas.delete(1.0, END)

        for linha in respostas:
            exibir_respostas.insert(END, linha + "\n\n")

    except Exception as e:
        exibir_respostas.insert(END, f"Erro: {str(e)}\n")

# Criação da janela principal
janela = Tk()
janela.title("ChatGPT - Perguntas e Respostas")
janela.geometry("1000x600")  # Tamanho inicial da janela
janela.configure(bg="#ecf0f1")

# Lista para armazenar as respostas
respostas = []

# Frame principal
frame_principal = Frame(janela, bg="#ffffff", bd=10, relief="ridge")
frame_principal.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Frame para a área de perguntas
frame_perguntas = Frame(frame_principal, bg="#3498db", bd=5, relief="flat")
frame_perguntas.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

# Frame para a área de respostas
frame_respostas = Frame(frame_principal, bg="#2ecc71", bd=5, relief="flat")
frame_respostas.pack(side=RIGHT, fill=BOTH, expand=True, padx=(10, 0))

# Listbox para exibir perguntas
lista_perguntas = Listbox(frame_perguntas, bg="#ffffff", fg="#2c3e50", font=("Helvetica", 12), borderwidth=2, relief="flat", selectbackground="#1abc9c")
lista_perguntas.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Área de texto para exibir perguntas e respostas
exibir_respostas = Text(frame_respostas, bg="#ffffff", fg="#2c3e50", font=("Helvetica", 12), borderwidth=2, relief="flat", wrap=WORD)
exibir_respostas.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Label para o campo de entrada
label_pergunta = Label(frame_perguntas, text="Faça sua Pergunta:", bg="#3498db", fg="#ffffff", font=("Helvetica", 14))
label_pergunta.pack(pady=10)

# Campo de entrada de dados
entrada_usuario = Text(frame_perguntas, height=2, bg="#ffffff", fg="#2c3e50", font=("Helvetica", 12), borderwidth=2, relief="flat", wrap=WORD)
entrada_usuario.pack(padx=10, pady=(0, 10), fill=X)

# Botão para enviar a pergunta
botao_perguntar = Button(frame_perguntas, text="Enviar Pergunta", font=("Helvetica", 14), command=obter_resposta, bg="#1abc9c", fg="#ffffff", relief="raised", activebackground="#16a085")
botao_perguntar.pack(pady=10)

# Configuração de tamanhos
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

# Inicia o loop principal da janela
janela.mainloop()
