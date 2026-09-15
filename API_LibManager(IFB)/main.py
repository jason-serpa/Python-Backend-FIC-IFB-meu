from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Livro(BaseModel):
    titulo:str
    autor:str

app = FastAPI()
livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo"},
    {"id": 3, "titulo": "Vidas Secas", "autor": "Graciliano Ramos"}
]

@app.get("/")
def inicio():
    return {"mensagem": "API de Livros"}
@app.get("/livros")
def listar_livros():
    return livros
@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int):
    for livro in livros:
        if livro["id"] == livro_id:
            return livro
    raise HTTPException(status_code=404, detail="LIVRO NÃO ENCONTRADO.")


@app.post("/livros", status_code=201)
def cadastrar_livro(livro: Livro):
    novo_livro = {
        "id": len(livros)+1,
        "titulo": livro.titulo,
        "autor": livro.autor
    }
    livros.append(novo_livro)
    return novo_livro


@app.put("/livros/{livro_id}")
def atualizar_livro(livro_id: int, livro_atualizado: Livro):
    for livro in livros:
        if livro["id"] == livro_id:
            livro["titulo"] = livro_atualizado.titulo
            livro["autor"] = livro_atualizado.autor
            return livro
    return {"mensagem": "Livro não encontrado."}
    

@app.delete("/livros/{livro_id}")
def excluir_livro(livro_id: int):
    for livro in livros:
        if livro["id"] == livro_id:
            livros.remove(livro)
            return {"mensagem": f"Livro '{livro['titulo']}' excluído com sucesso"}
    return {"mensagem": "Livro não encontrado"}