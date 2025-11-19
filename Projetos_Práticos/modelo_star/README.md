# atv_regressao_logistica_llm
Desafio Prático Regressão Logistica do urso de LLM - Rocketseat

Neste desafio, você atuará como cientista de dados, com a missão de identificar estrelas de nêutrons pulsares reais a partir de observações astronômicas captadas por radiotelescópios. O contexto envolve a aplicação de técnicas de classificação para diferenciar pulsares de outras fontes astrofísicas ou ruído, utilizando dados estatísticos extraídos de sinais de rádio.

O objetivo é treinar um modelo de regressão logística para classificar corretamente as observações como pulsares ou não-pulsares, utilizando apenas os atributos fornecidos. O arquivo de dados está disponível em pulsar.csv.

Descrição do Dataset: 

O dataset é composto por 17.898 observações, cada uma representando medições estatísticas de sinais obtidos por radiotelescópios. Abaixo estão os oito atributos disponíveis:

Mean of the integrated profile Média do perfil integrado do sinal, que representa a média da intensidade do sinal ao longo do tempo.

Standard deviation of the integrated profile Desvio padrão do perfil integrado, indicando a variação da intensidade em torno da média.

Excess kurtosis of the integrated profile Curtose excessiva do perfil integrado, que mede a "cauda" da distribuição do sinal em relação a uma distribuição normal.

Skewness of the integrated profile Assimetria do perfil integrado, representando o grau de distorção da distribuição do sinal em torno da média.

Mean of the DM-SNR curveMédia da curva DM-SNR (medida da razão sinal-ruído em função da dispersão), que quantifica a intensidade média do sinal ajustado por diferentes dispersões.

Standard deviation of the DM-SNR curveDesvio padrão da curva DM-SNR, indicando a variabilidade da razão sinal-ruído em diferentes dispersões.

Excess kurtosis of the DM-SNR curveCurtose excessiva da curva DM-SNR, avaliando a presença de picos extremos na distribuição da razão sinal-ruído.

Skewness of the DM-SNR curveAssimetria da curva DM-SNR, que mostra a inclinação da distribuição da razão sinal-ruído em relação à média.

target_classClasse alvo binária que indica o tipo de objeto:
1: Pulsares reais (estrelas de nêutrons altamente magnetizadas)
0: Não-pulsares (ruído ou outras fontes astrofísicas)
