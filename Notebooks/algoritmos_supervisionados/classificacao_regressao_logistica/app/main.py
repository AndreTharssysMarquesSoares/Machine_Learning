from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib

app = FastAPI()

class Request_body(BaseModel):
    A_id: int
    Size: float
    Weight: float
    Sweetness: float
    Crunchiness: float
    Juiciness: float
    Ripeness: float
    Acidity: float
    
modelo_qualidade =joblib.load('modelo_classificacao_frutas.pkl')

@app.post('/classify')
def predict(data: Request_body):
    #Preparar features
    input_features = [[data.Size, data.Weight, data.Sweetness, data.Crunchiness, data.Juiciness, data.Ripeness, data.Acidity]]
    
    # Classificar fruta
    y_pred = modelo_qualidade.predict(input_features)[0].astype(int)
    y_prob = modelo_qualidade.predict_proba(input_features)[0].astype(float)
    
    resposta = 'Boa' if y_pred ==1 else 'Ruim'
    probabilidade = y_prob[y_pred]
    
    return {'qualidade': resposta, 'probabilidade': probabilidade}

#uvicorn main:app --host 0.0.0.0 --port 80 --reload

