from flask import Flask, request, jsonify
from pydantic import BaseModel
from flask_pydantic import validate
import joblib
import pandas as pd 

# Criar instância do Flask
app = Flask(__name__)

# Classe que receberá os dados do formulário
class request_body(BaseModel):
    Genero_Masculino: int
    Idade: int
    Historico_Familiar_Sobrepeso: int
    Consumo_Alta_Caloria_Com_Frequencia: int
    Consumo_Vegetais_Com_Frequencia: int
    Refeicoes_Dia: int
    Consumo_Alimentos_entre_Refeicoes: int
    Fumante: int
    Consumo_Agua: int
    Monitora_Calorias_Ingeridas: int
    Nivel_Atividade_Fisica: int
    Nivel_Uso_Tela: int
    Consumo_Alcool: int
    Transporte_Automovel: int
    Transporte_Bicicleta: int
    Transporte_Motocicleta: int
    Transporte_Publico: int
    Transporte_Caminhada: int
    
# Carregar modelo
modelo_obesidade = joblib.load(".\modelo_obesidade.pkl")

@app.route('/predict', methods=['POST'])
@validate(body=request_body)
def predict(body: request_body):
    #Tranformar body em DF
    df_predict = pd.DataFrame(body.model_dump(), index=[1])
    
    # Incluir faixa etaria
    bins_idade = [10,20,30,40,50,60,70]
    bins_ordinal_idade = [0,1,2,3,4,5]
    df_predict['Faixa_Etaria'] = pd.cut(x = df_predict.Idade, bins=bins_idade, labels= bins_ordinal_idade, include_lowest=True)
    
    # Deixar as k melhores features 
    df_predict = df_predict[[
                            'Historico_Familiar_Sobrepeso',
                            'Consumo_Alta_Caloria_Com_Frequencia',
                            'Consumo_Alimentos_entre_Refeicoes', 
                            'Monitora_Calorias_Ingeridas',
                            'Nivel_Atividade_Fisica',
                            'Nivel_Uso_Tela',
                            'Transporte_Caminhada',
                            'Faixa_Etaria'
    ]]
    
    #Predizer a classificacao
    y_pred = modelo_obesidade.predict(df_predict)[0].astype(int)
    
    #Retornar valores na API
    return jsonify({'obesidade': y_pred.tolist()})

# Executar o app Flask
if __name__ == '__main__':
    app.run(port=5000, debug=True)

# Para rodar
# python api_modelo_obesidade.py
# Utilize o thunder cliente, postman, ou algum test de api similar para  realziar a predicao 