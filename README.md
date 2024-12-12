# arquitetura_de_sistemas


# API de Contatos - FastAPI

## Descrição

Esta API RESTful, desenvolvida com o FastAPI, permite gerenciar sua agenda de contatos de forma fácil e intuitiva.

* **Criação:** ➕ Adicione novos contatos à sua agenda.
* **Edição:**  Modifique as informações dos seus contatos.
* **Busca:**  Encontre rapidamente o contato que você precisa.
* **Deleção:** ❌ Remova contatos indesejados.

## Pré-requisitos

* Python 3.6+
* FastAPI
* Uma ferramenta para executar servidores web (e.g., Uvicorn)

## Instalação

1. **Clone este repositório:**
   ```bash
   git clone https://seu-repositorio.git
   ```


## Endpoints

* **GET** `http://127.0.0.1:8000/contatos` 🟢 Lista todos os contatos.
* **POST** `http://127.0.0.1:8000/contatos` 🟢 Cria um novo contato.
* **PUT** `http://127.0.0.1:8000/contatos/1` 🟢 Atualiza um contato.
* **DELETE** `http://127.0.0.1:8000/contatos/1` 🟢 Deleta um contato.
