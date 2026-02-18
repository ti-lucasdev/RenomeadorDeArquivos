import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
import re

ARQUIVO_CONFIG = 'config.json'
PADRAO_IDIOMAS = [
    'PORTUGUÊS', 'ESPANHOL', 'FRANCÊS', 'ÁRABE', 'ALEMÃO', 'BÚLGARO', 
    'COREANO', 'CROATA', 'CHINÊS (MANDARIM)', 'ESLOVACO', 'FILIPINO (TAGALO)', 
    'GREGO', 'HOLANDÊS', 'HÍNDI (OU OUTROS IDIOMAS DA ÍNDIA)', 'INDONÉSIO', 
    'INGLÊS', 'ITALIANO', 'JAPONÊS', 'MALAIO', 'POLONÊS', 'ROMENO', 'RUSSO', 
    'TCHECO', 'TURCO', 'UCRANIANO', 'HÚNGARO', 'BENGALI (BANGLADESH)', 
    'ESLOVENO', 'TAILANDÊS', 'URDU', 'HEBRAICO (ISRAEL)', 'SÉRVIO', 'VIETNAMITA'
]

def carregar_configuracoes():
    if os.path.exists(ARQUIVO_CONFIG):
        with open(ARQUIVO_CONFIG, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return PADRAO_IDIOMAS

def salvar_configuracoes(idiomas):
    with open(ARQUIVO_CONFIG, 'w', encoding='utf-8') as arquivo:
        json.dump(idiomas, arquivo, ensure_ascii=False, indent=4)

def extrair_numero(nome_arquivo):
    nome_sem_ext = os.path.splitext(nome_arquivo)[0]
    numeros = re.findall(r'\d+', nome_sem_ext)
    return int(numeros[-1]) if numeros else 0

def processar_renomeacao(pasta, idiomas):
    try:
        arquivos = [
            f for f in os.listdir(pasta) 
            if os.path.isfile(os.path.join(pasta, f)) 
            and not f.startswith('.') 
            and f.lower() not in ['config.json', 'desktop.ini', 'thumbs.db']
        ]
        
        arquivos.sort(key=extrair_numero)
        contador = 0

        for i, arquivo in enumerate(arquivos):
            indice_idioma = i // 5
            
            if indice_idioma >= len(idiomas):
                break

            numero_no_lote = (i % 5) + 1
            
            caminho_antigo = os.path.join(pasta, arquivo)
            _, extensao = os.path.splitext(arquivo)
            
            # Aqui está a estrutura correta: Idioma - 1, Idioma - 2
            novo_nome = f"{idiomas[indice_idioma]} - {numero_no_lote}{extensao}"
            caminho_novo = os.path.join(pasta, novo_nome)

            if not os.path.exists(caminho_novo):
                os.rename(caminho_antigo, caminho_novo)
                contador += 1

        messagebox.showinfo("Sucesso", f"Processo concluído! {contador} arquivos renomeados.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao renomear: {e}")

def abrir_configuracoes():
    def salvar():
        nova_lista = [lang.strip() for lang in entrada.get("1.0", tk.END).split('\n') if lang.strip()]
        salvar_configuracoes(nova_lista)
        janela_config.destroy()
        messagebox.showinfo("Salvo", "Sequência atualizada com sucesso!")

    janela_config = tk.Toplevel(root)
    janela_config.title("Configurar Idiomas")
    janela_config.geometry("400x500")

    tk.Label(janela_config, text="Idiomas (um por linha):").pack(pady=10)
    
    entrada = tk.Text(janela_config, width=40, height=20)
    entrada.insert("1.0", "\n".join(carregar_configuracoes()))
    entrada.pack(pady=5)

    tk.Button(janela_config, text="Salvar", command=salvar).pack(pady=10)

def selecionar_pasta_e_renomear():
    pasta = filedialog.askdirectory()
    if pasta:
        idiomas = carregar_configuracoes()
        processar_renomeacao(pasta, idiomas)

# --- INÍCIO DA APLICAÇÃO ---
root = tk.Tk()
root.title("Renomeador Revídia")
root.geometry("350x150")

tk.Button(root, text="1. Configurar Idiomas", command=abrir_configuracoes, width=30).pack(pady=15)
tk.Button(root, text="2. Selecionar Pasta e Renomear", command=selecionar_pasta_e_renomear, width=30).pack(pady=5)

root.mainloop()