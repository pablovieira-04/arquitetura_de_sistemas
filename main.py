from typing import List

from fastapi import FastAPI, Form, HTTPException, Query

app = FastAPI()

# In-memory storage for contacts
contacts: List[dict] = []

@app.get("/contatos")
async def listar_contatos():
  """
  Recupera a lista de todos os contatos.
  """
  return {
      "status": "success",
      "message": "Contatos recuperados com sucesso.",
      "data": contacts
  }

@app.get("/contacts/{contact_id}")
async def obter_contato_por_id(contact_id: int):
  """
  Recupera um contato específico pelo seu ID.
  """
  for contact in contacts:
      if contact["id"] == contact_id:
          return {
              "status": "success",
              "message": "Contato recuperado com sucesso.",
              "data": contact
          }
  raise HTTPException(status_code=404, detail="Contato não encontrado.")

@app.get("/contacts_search")
async def buscar_contatos_por_nome(name: str = Query(...)):
  """
  Busca contatos por nome (pesquisa por substring).
  """
  matching_contacts = [contact for contact in contacts if name.lower() in contact["name"].lower()]
  if matching_contacts:
      return {
          "status": "success",
          "message": "Contatos recuperados com sucesso.",
          "data": matching_contacts
      }
  raise HTTPException(status_code=404, detail="Nenhum contato encontrado com o nome fornecido.")

@app.post("/contatos")
async def criar_contato(
  name: str = Form(...),
  phone: str = Form(...),
  email: str = Form(...)
):
  """
  Adiciona um novo contato à agenda.
  """
  new_id = len(contacts) + 1  # Gera um ID simples
  contact = {
      "id": new_id,
      "name": name,
      "phone": phone,
      "email": email
  }
  contacts.append(contact)
  return {
      "status": "success",
      "message": "Contato adicionado com sucesso.",
      "data": contact
  }

@app.put("/contacts/{contact_id}")
async def atualizar_contato(
  contact_id: int,
  name: str = Form(...),
  phone: str = Form(...),
  email: str = Form(...)
):
  """
  Atualiza os detalhes de um contato existente.
  """
  for contact in contacts:
      if contact["id"] == contact_id:
          contact.update({"name": name, "email": email, "phone": phone})
          return {
              "status": "success",
              "message": "Contato atualizado com sucesso.",
              "data": contact
          }
  raise HTTPException(status_code=404, detail="Contato não encontrado.")

@app.delete("/contacts/{contact_id}")
async def deletar_contato(contact_id: int):
    """
    Remove um contato da agenda.
    """
    for index, contact in enumerate(contacts):
        if contact["id"] == contact_id:
            deleted_contact = contacts.pop(index)
            return {
                "status": "success",
                "message": "Contato deletado com sucesso.",
                "data": deleted_contact
            }
    raise HTTPException(status_code=404, detail="Contato não encontrado.")