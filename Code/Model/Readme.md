--> Previsão com AUTO-ARIMA:




A função auto_arima ajusta o melhor modelo ARIMA para uma série temporal univariada de acordo com um critério de informação fornecido (AIC, AICc, BIC ou HQIC). A função realiza uma pesquisa (seja por etapas ou paralelizada) sobre possíveis pedidos de modelo e sazonal dentro das restrições fornecidas e seleciona os parâmetros que minimizam a métrica fornecida


--> Previsão com Prophet





A modelagem do Prophet assume que existem duas fontes de incerteza nos dados:

Resíduos gaussianos ao redor da linha de tendência
Alterando os valores da inclinação
Ao ajustar, o Prophet encontra os melhores pontos nos dados de treinamento para mudanças de tendência para melhor ajustar os dados – supõe-se que a tendência seja linear em qualquer ponto, mas a inclinação da tendência pode mudar. 
Naturalmente, quanto mais mudanças de tendência forem encontradas, e quanto maior for o delta entre encostas adjacentes, maior será a incerteza nos valores futuros, como pode ser visto nestes exemplos.

Cerca de 98% do tempo é gasto em “predict_uncertainty”. Esta função cria “yhat_upper” e “yhat_lower” no DataFrame resultante, que são as bordas de um intervalo de confiança de 80% (ou qualquer outro valor dado em interval_width) – onde os pontos reais provavelmente estarão.