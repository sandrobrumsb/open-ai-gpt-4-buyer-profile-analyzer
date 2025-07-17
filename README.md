# Projeto: 🤖🧠 Identificação de Perfis de Compra de cliente com API da OpenAI modelo GPT-4
---

**O que ele faz:**  
Este script envia um conjunto de dados contendo compras de 15 clientes para o modelo `gpt-4`, com o objetivo de **classificar o perfil de compra de cada cliente em três palavras**.

O script realiza:

- Leitura automática do arquivo `.csv` com os dados
- Geração de prompts estruturados para o modelo
- Estimativa simples do número de tokens utilizados
- Envio da requisição via API da OpenAI
- Impressão da resposta com os perfis identificados

---

## 🚀 Como rodar os scripts:

Siga os passos abaixo para executar qualquer um dos projetos deste repositório:

### 1. Clone o repositório

```bash
git clone https://github.com/sandrobrumsb/open-ai-gpt-4-buyer-profile-analyzer.git
```
### 2. Instale as 📚 Bibliotecas:
```bash
pip install -r requirements.txt
```
### 3. 📦 Crie o Arquivo `.env`:

- Insira no arquivo `.env` com suas chaves de API:
  ```env
  OPENAI_API_KEY='your_openai_key_here'
---
