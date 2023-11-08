from fastapi import FastAPI


app = FastAPI()

vendas = {

    1: {"item": "lata", "preco_unitario": 6, "quantidade": 5},
    2: {"item": "coca-cola 2 L", "preco_unitario": 11, "quantidade": 6},
    3: {"item": "coca-cola 750ml", "preco_unitario": 6, "quantidade": 10},
    4: {"item": "energetico", "preco_unitario": 11, "quantidade": 12},
}

@app.get("/")
def home():
    return "Minha api está no ar"

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return  vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente"}
