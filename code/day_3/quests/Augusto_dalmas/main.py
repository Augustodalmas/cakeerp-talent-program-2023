from fastapi import FastAPI
from typing import Union

app = FastAPI() #Importa o FRAMEWORK

@app.get("/status") #Decora a Funçao get, que está internamente criada no framework
async def root(): 
    return {"Status" : "it's alive"} #Parametro de mensagem sem tipagem