# Importa a classe OpenAI para interação com a API da OpenAI
from openai import OpenAI

# Importa a função para carregar variáveis de ambiente do arquivo .env
from dotenv import load_dotenv

# Importa o módulo os para acessar variáveis de ambiente
import os

# Carrega as variáveis de ambiente definidas em um arquivo .env
load_dotenv()

# Cria um cliente OpenAI usando a chave de API armazenada na variável de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define o modelo a ser utilizado
model = "gpt-4"


# Função para carregar dados de um arquivo de texto
def to_load(file_name):
    try:
        # Abre o arquivo em modo leitura com codificação UTF-8
        with open(file_name, "r", encoding="utf-8") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        # Captura e exibe erros de entrada/saída
        print(f"error: {e}")


# Prompt do sistema: instruções que definem o comportamento do modelo
prompt_system = """
Identifique o perfil de compra para cada client a seguir.
O formato de saída deve ser:
client - descreva o perfil do client em 3 palavras.
"""

# Carrega os dados dos clientes a partir de um arquivo CSV
prompt_user = to_load(r"dados\lista_de_compras_15_clientes.csv")

# Estima o número de tokens na entrada (dividindo pelo número de palavras como aproximação)
number_of_tokens = len((prompt_system + prompt_user).split())
print(f"Estimativa de tokens de entrada: {number_of_tokens}")

# Informa o modelo selecionado
print(f"Modelo Escolhido: {model}")

# Cria a lista de mensagens para o modelo de chat da OpenAI
message_list = [
    {
        "role": "system",  # Define o comportamento e as instruções gerais
        "content": prompt_system,
    },
    {"role": "user", "content": prompt_user},  # Fornece os dados de entrada do usuário
]

# Envia a requisição para a API da OpenAI e armazena a resposta
response = client.chat.completions.create(messages=message_list, model=model)

# Exibe a resposta do modelo
print(response.choices[0].message.content)
