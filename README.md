
### Infnet
## Projeto De Bloco - IOT e Data Science


Este projeto simula como seria um dispositivo IOT medindo a qualidade do ar e temperatura de Curitiba, e utilizando algoritmos de forecasting (ARIMA e FBPROPHET) para apontar melhores estratégias a serem tomadas na controle de qualidade do ar.

A qualidade do ar é medida com um sesor de particulas que mede a concentração de PM2.5.
As PM2,5 são um tipo de partículas inaláveis, de diâmetro inferior a 2,5 micrometros (µm) e constituem um elemento de poluição atmosférica.
Em Code temos o algoritmo de forecasting ARIMA que preve a qualidade do ar 24 meses no futuro.

A temperatura é obtida com um sensor simples dd18b20.



# Descrição do projeto

- Um exemplo simples e prático de um raspberry com sensor de qualidade de ar, na prática, pode sem encontrado neste projeto:
https://github.com/otonchev/grove_dust
O módulo do sensor possui um código em C, cujo binario oferece a saida do leitor.
Então um script em Python, obtem esse dados do sensor, e anota no banco de dados com a leitura e o datetime.

Nosso projeto se inicia com esse dados já coletados, simulados e é organizado da seguinte forma:

* Pastas:
  * Code: Onde é feita a analise do problema, codigos de python e notebook.
    * DataPrep: Esta pasta hospeda o código para aquisição e compreensão de dados
    * Model: Esta pasta contém código para modelagem e atividades dos algoritmos de previsão 

  * Data: Contém todos os datasets utilizados no projeto
    * Raw: raw datasets
    * Processed: datasets processados
    * Modeling: lista de conjunto de features

