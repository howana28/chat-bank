# 🏦 KORU Bank - Chatbot Bancário com Flask

Este projeto é um chatbot bancário simples, desenvolvido com Python (Flask) no backend e HTML/CSS/JS no frontend. Ele simula interações básicas com um cliente utilizando uma máquina de estados finitos (FSM).

## 🚀 Funcionalidades

- Interface de chat amigável e responsiva
- Reconhecimento de intenções do usuário
- Máquina de estados (FSM) para controlar o fluxo da conversa
- Backend em Flask para manipular as mensagens

## 📁 Estrutura de Pastas

chatbot-bancario/
│
├── app.py # Arquivo principal Flask
├── intents.py # Reconhece intenções do usuário
├── fsm.py # Lógica de transição da FSM
├── requirements.txt # Dependências do projeto
│
├── templates/
│ └── chatbot-bancario.html # Interface principal do chatbot
│
└── static/
├── css/
│ └── style.css # Estilo da interface
└── js/
└── script.js # Lógica do frontend (envio de mensagens)

