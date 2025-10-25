from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    nome: str
    preco: float

@app.get("/")
def read_root():
    return {"message": "API de Exemplo com FastAPI"}

@app.get("/dobro/{numero}")
def dobro(numero: int):
    return {"dobro": numero * 2}

@app.post("/produto/")
def produto(produto: Produto):
    desconto = produto.preco * 0.9
    return {"valor_com_desconto": desconto}

@app.post("/cadastro/")
def cadastro(produto: Produto):
    with open("produtos.txt", "a") as f:
        f.write(f"{produto.nome},{produto.preco}\n")
    return {"message": "Produto cadastrado"}
