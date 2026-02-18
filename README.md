# Renomeador Revídia (Batch File Renamer)

## Descrição
Automação desenvolvida em Python para otimizar o fluxo de trabalho de design e exportação de arquivos em lote. O sistema lê uma pasta com múltiplos arquivos (ex: exportações do Canva) e os renomeia automaticamente em blocos de 5, aplicando uma sequência de idiomas definida pelo usuário.

## Funcionalidades
* **Interface Gráfica (GUI):** Construída com `tkinter` para facilitar o uso por usuários finais.
* **Memória de Configuração:** Salva a última sequência de idiomas inserida pelo usuário utilizando um arquivo `.json`.
* **Lógica de Lotes:** Utiliza divisão matemática para renomear os arquivos em grupos exatos (ex: 5 arquivos recebem o prefixo "Português", os próximos 5 "Espanhol", etc.).
* **Preservação de Formato:** Extrai e mantém a extensão original de qualquer arquivo (`.mp4`, `.jpg`, `.txt`, etc.).
* **Ordenação Inteligente:** Usa Expressões Regulares (`re`) para ler a numeração real do arquivo, evitando falhas de ordenação do sistema operacional (ex: ler 1, 2, 10 em vez de 1, 10, 2).

## Tecnologias Utilizadas
* Python 3
* Tkinter (Interface Gráfica)
* Bibliotecas nativas: `os`, `json`, `re`

## Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/renomeador-revidia.git](https://github.com/seu-usuario/renomeador-revidia.git)