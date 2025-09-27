# pip install openai -
from openai import OpenAI # biblioteca do chatgpt

# inicializar o cliente 
cliente = OpenAI(api_key="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")

# https://abre.ai/chaveopenai (link da chave de API, fornecida pelo professor)
# OpenAi dashboard -> conta de vocês (para solicitar nossas proprias chaves)
# chat é uma IA de completações de informação

# faz a chamada para a OpenAI
resposta = cliente.chat.completions.create(
    model='gpt-4o-mini', # gpt-4, gpt-5, gpt-4o
    messages=[
        {"role": "system", "content": "Você é um assistente que responde em portugues"},
        {"role": "user", "content": "Quantas variedades de plantas tem no mundo?"}
           
        
    ]
)

# Exibe resposta do modelo
print(resposta.choices[0].message.content)