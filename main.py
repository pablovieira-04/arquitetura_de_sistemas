from typing import List

from fastapi import FastAPI, Form, HTTPException, Query

app = FastAPI()

# Armazenamento em memória para contatos
contatos = []

@app.get("/contatos")
async def listar_contatos():
  """
  Recupera a lista de todos os contatos.
  """
  return {
      "status": "successo",
      "mensagem": "Contatos recuperados com sucesso.",
      "dados": contatos
  }

@app.get("/contatos/{contato_id}")
async def obter_contato_por_id(contato_id: int):
  """
  Recupera um contato específico pelo seu ID.
  """
  for contato in contatos:
    if contato["id"] == contato_id:
      return {
          "status": "successo",
          "mensagem": "Contato recuperado com sucesso.",
          "dados": contato
      }
  raise HTTPException(status_code=404, detail="Contato não encontrado.")

@app.get("/contatos_pesquisa")
async def buscar_contatos_por_nome(nome: str = Query(...)):
  """
  Busca contatos por nome (pesquisa por substring).
  """
  contatos_encontrados = [contato for contato in contatos if nome.lower() in contato["nome"].lower()]
  if contatos_encontrados:
    return {
        "status": "successo",
        "mensagem": "Contatos recuperados com sucesso.",
        "dados": contatos_encontrados
    }
  raise HTTPException(status_code=404, detail="Nenhum contato encontrado com o nome fornecido.")

@app.post("/contatos")
async def criar_contato(
  nome: str = Form(...),
  telefone: str = Form(...),
  email: str = Form(...)
):
  """
  Adiciona um novo contato à agenda.
  """
  novo_id = len(contatos) + 1  # Gera um ID simples
  contato = {
      "id": novo_id,
      "nome": nome,
      "telefone": telefone,
      "email": email
  }
  contatos.append(contato)
  return {
      "status": "successo",
      "mensagem": "Contato adicionado com sucesso.",
      "dados": contato
  }

@app.put("/contatos/{contato_id}")
async def atualizar_contato(
  contato_id: int,
  nome: str = Form(...),
  telefone: str = Form(...),
  email: str = Form(...)
):
  """
  Atualiza os detalhes de um contato existente.
  """
  for contato in contatos:
    if contato["id"] == contato_id:
      contato.update({"nome": nome, "email": email, "telefone": telefone})
      return {
          "status": "successo",
          "mensagem": "Contato atualizado com sucesso.",
          "dados": contato
      }
  raise HTTPException(status_code=404, detail="Contato não encontrado.")

@app.delete("/contatos/{contato_id}")
async def deletar_contato(contato_id: int):
  """
  Remove um contato da agenda.
  """
  for indice, contato in enumerate(contatos):
    if contato["id"] == contato_id:
      contato_deletado = contatos.pop(indice)
      return {
          "status": "successo",
          "mensagem": "Contato deletado com sucesso.",
          "dados": contato_deletado
      }
  raise HTTPException(status_code=404, detail="Contato não encontrado.")