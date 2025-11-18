from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Criar uma instancia para o fastApi
app = FastAPI()

#Criar uma classe que terá os dados do request body para a API
class request_body(BaseModel):
    horas_estudo: float
    
# Carregar modelo para predição
modelo_pontuacao = joblib.load('.\modelo_regressao.pkl')

@app.post('/predict')
def predict(data: request_body):
    # Preparar os dados para predicao
    input_feature = [[data.horas_estudo]]
    
    # Realizar a predicao
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)
    
    return {'pontuacao_teste': y_pred.tolist()}