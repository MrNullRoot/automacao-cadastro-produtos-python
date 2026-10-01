# automacao-cadastro-produtos-python

Praticando Automação de Dados e Integração com Python, Pandas e HTML/JS 🚀

## O que faz

- Lê um CSV (código, nome, categoria e preço) com **pandas**.
- Controla digitação e navegação no formulário web local com **pyautogui**.
- A página em **HTML/CSS/JS** registra cada cadastro em tempo real numa tabela e reseta os campos automaticamente.

## Tecnologias

Python, pandas, pyautogui, HTML, CSS e JavaScript.

## Arquivos

- `script.py` – script principal da automação
- `auxiliar.py` – utilitário para descobrir as coordenadas do mouse na tela (usadas para posicionar os cliques da automação
- `index.html` – formulário e tabela
- `produtos.csv` – 8 produtos fictícios para teste
- `requirements.txt` – dependências do projeto

## Aprendizados

- Sincronismo entre o script Python e a renderização do navegador
- Condições de corrida e controle de foco (autofocus e eventos JS)
- Limpeza de dados para evitar erros de tipagem na digitação automatizada

## Como rodar

1. Instale as dependências: `pip install -r requirements.txt`
2. No VS Code, abra o `index.html` com a extensão **Live Server** (porta 5500)
3. Execute `python script.py` e não mexa no mouse nem no teclado durante a automação

## Próximo passo

Refatorar o fluxo com Playwright (headless, independente da resolução de tela).

> Os dados do CSV são fictícios, usados apenas para estudo.
