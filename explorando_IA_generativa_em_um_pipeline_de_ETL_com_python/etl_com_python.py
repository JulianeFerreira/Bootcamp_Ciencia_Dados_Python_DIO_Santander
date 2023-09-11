# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BFGTcuAWl8i4EXRcDwvFDxnOu_Y_Y6zH

#Santander Dev Week 2023 (ETL com Python)

**Contexto:** Você é um cientista de dados no Santander e recebeu a tarefa de envolver seus clientes de maneira mais personalizada. Seu objetivo é usar o poder da IA Generativa para criar mensagens de marketing personalizadas que serão entregues a cada cliente.

**Condições do Problema:**

1. Você recebeu uma planilha simples, em formato CSV ('SDW2023.csv'), com uma lista de IDs de usuário do banco:
  ```
  UserID
  1
  2
  3
  4
  5
  ```
2. Seu trabalho é consumir o endpoint `GET https://sdw-2023-prd.up.railway.app/users/{id}` (API da Santander Dev Week 2023) para obter os dados de cada cliente.
3. Depois de obter os dados dos clientes, você vai usar a API do ChatGPT (OpenAI) para gerar uma mensagem de marketing personalizada para cada cliente. Essa mensagem deve enfatizar a importância dos investimentos.
4. Uma vez que a mensagem para cada cliente esteja pronta, você vai enviar essas informações de volta para a API, atualizando a lista de "news" de cada usuário usando o endpoint `PUT https://sdw-2023-prd.up.railway.app/users/{id}`.
"""

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

"""## **E**xtract

Extraia a lista de IDs de usuário a partir do arquivo CSV. Para cada ID, faça uma requisição GET para obter os dados do usuário correspondente.
"""

import pandas as pd

df = pd.read_csv('SDW2023.csv.txt')
user_ids = df['UserID'].tolist()
print(user_ids)

import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

"""## **T**ransform

Utilize a API do OpenAI GPT-4 para gerar uma mensagem de marketing personalizada para cada usuário.
"""

!pip install openai

openai_api_key = 'TODO'

import openai

openai.api_key = openai_api_key

def generate_ai_news(user_name):

    return f"Notícia gerada para {user_name}: Organizar suas finanças é fundamental para garantir um futuro estável."


user_names = ["Name1", "Name2", "Name3"]

for user_name in user_names:
    news = generate_ai_news(user_name)
    print(news)

"""## **L**oad

Atualize a lista de "news" de cada usuário na API com a nova mensagem gerada.
"""

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")