# 🧾 Automação de Emissão de Notas Fiscais com Python e Selenium

Automatizando o processo de emissão de notas fiscais!
Este projeto lê dados de uma planilha Excel e preenche automaticamente um formulário HTML para gerar notas fiscais.

## 🧠 O que ele faz?
👉 Faz login no sistema (simulado em HTML).
👉 Lê os dados da planilha `NotasEmitir.xlsx`.
👉 Preenche automaticamente os campos do formulário (`index.html`).
👉 Emite as notas e reinicia o formulário para o próximo cliente.

## 🛠️ Tecnologias usadas
- Python 🐍
- Selenium 🌐
- pandas 📊
- WebDriver Manager 🔧
- HTML (para simulação do sistema) 🧠

## 📂 Estrutura de arquivos
- `automação_NF-E1.py` → Script principal
- `login.html` → Tela de login (simulada)
- `index.html` → Formulário de emissão de nota (simulado)
- `NotasEmitir.xlsx` → Dados das notas fiscais a serem emitidas

## 💡 Como rodar
1. Tenha Python instalado na sua máquina.
2. Instale as dependências:
```bash
pip install selenium pandas webdriver-manager
