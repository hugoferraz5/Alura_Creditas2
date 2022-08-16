# Alura_Creditas
Projeto de regressão com objetivo de obter predições de valores de imóveis da cidade de São Paulo.

<div align="center">
<img src="https://user-images.githubusercontent.com/91911052/184797458-b67d17bd-d04f-4fb5-bfa0-79617cb8a3b9.jpg" width="700px" />
</div>

# 1 Sobre a Creditas
O brasileiro tem fácil acesso às piores taxas de juros, e a Creditas nasceu para mudar essa realidade. Eles combatem o mau endividamento com um crédito de qualidade, que permite que os bens levem ainda mais longe. O objetivo é garantir o seu progresso financeiro e ajudar a realizar projetos de vida. Fintech criada em 2012, a Creditas é especialista em empréstimos com imóvel ou carro como garantia; empresa já emprestou R$ 300 milhões no Brasil e tem 370 funcionários.

# 2 Apresentação
Nesse projeto proposto pela Alura, obtive um modelo de Regressão com o objetivo de predizer quanto vale um determinado imóvel na cidade de São Paulo que é usado como garantia de um empréstimo feito por um cliente na empresa Creditas. A fim de obter valores mais próximos possíveis do real, fiz uma análise exploratória dos dados existentes de imóveis com várias informações para facilitar o entendimento do negócio e conseguir o objetivo final. 
Informações sobre a Creditas podem ser encontradas nesse link: <a href="https://www.creditas.com/quem-somos">siteCreditas</a>

O projeto completo pode ser encontrado neste link:
<a href="https://github.com/hugoferraz5/Webmotors_leads/blob/main/Classifica%C3%A7%C3%A3o_webmotors.ipynb">ProjetoAlura</a>

|Atributo | Definição
------------ | -------------
|	Bairro	| Bairro da cidade
|	Metragem | Metragens dos imóveis
|	Quartos	| Quantidade de quartos
|	Banheiros |	Quantidade de banheiros
| Vagas |	Quantidade de vagas
|	Valor_anuncio |	Valor dos imóvies
|	Valor_m2	| Valor por metro quadrado dos imóveis
|	Rua |	Nome das ruas 
|	cep |	Cep
|	setor_censo |	Setor censitário
|	Cod_distrito |	Códigos dos distritos
|	Nome_do_distrito |	Nomes dos distritos
|	Situacao_setor |	Situação do setor 
|	Tipo_setor |	Tipo do setor (0 ou 1)
|	V001 |	Domicílios particulares permanentes ou pessoas responsáveis por domicílios particulares permanentes
|	V002	| Moradores em domicílios particulares permanentes ou população residente em domicílios particulares permanentes
|	V003	| Média do número de moradores em domicílios particulares permanentes (obtida pela divisão de Var2 por Var1)
|	V004	| Variância do número de moradores em domicílios particulares permanentes
|	V005 | Valor do rendimento nominal médio mensal das pessoas responsáveis por domicílios particulares permanentes (com e sem rendimento)
|	V006	| Variância do rendimento nominal mensal das pessoas responsáveis por domicílios particulares permanentes (com e sem rendimento)
|	V007	| Valor do rendimento nominal médio mensal das pessoas responsáveis por domicílios particulares permanentes (com rendimento)
|	V008 |	Variância do rendimento nominal mensal das pessoas responsáveis por domicílios particulares permanentes (com rendimento)
|	V009 |	Valor do rendimento nominal médio mensal das pessoas de 10 anos ou mais de idade (com e sem rendimento)
|	V010 |	Variância do rendimento nominal mensal das pessoas de 10 anos ou mais de idade (com e sem rendimento)
|	V011 |	Valor do rendimento nominal médio mensal das pessoas de 10 anos ou mais de idade (com rendimento)
|	V012	| Variância do rendimento nominal mensal das pessoas de 10 anos ou mais de idade (com rendimento)

# 3 Premissas de negócio
* Dados do IBGE dos valores censitários foram fundamentais para obter mais informações
* Outros dados como as geocodificações e dados de São Paulo também foram excenciais nas análises
* Os gráficos ajudaram a ter mais clareza nas análises
* O valor por metro quadrado auxiliou nas análises exploratórias
* O histórico de cada imóvel ajudou nas conclusões

# 4 Passo a passo da solução

* **Questão de Negócios** - Fazer a predição de quanto vale um determinado imóvel na cidade de São Paulo que é usado como garantia de um empréstimo feito por um cliente na empresa Creditas.
* **Entendimento do negócio** - Entender as informações dos imóveis através dos dados disponibilizados. A partir desses dados, fazer as análises.
* **Coleta de Dados** - Coletar os dados dos imóveis.
* **Limpeza dos Dados** - Fazer a limpeza dos dados se existirem valores discrepantes e valores vazios através da linguagem Python. 
* **Exploração dos Dados** - Explorar os dados através de respostas à perguntas do CEO da empresa, achar bons insights pelas hipóteses levantadas e apresenta-los por meio de gráficos.
* **Modelagem dos Dados** - Fazer boas modelagens(correlações, reescalonamento, codificações, frequência dos dados) afim de facilitar as leituras dos modelos de Machine Learning. Achar os melhores recursos para os algoritmos.
* **Algoritmo de Machine Learning** - Com os dados modelados, vamos usar alguns algoritmos de Machine Learning de regressão para achar a melhor acurácia e baixos erros. Uso de Validação Cruzada e hiperparâmetros para deixa-la  ainda mais precisos os modelos e colocar em prática no final.
* **Avaliação de Algoritmo** - Comparação dos resultados dos algoritmos de regressão usados e utilizar o de melhor acurácia e baixos erros para colocar em prática a questão de negócios.

# 5 Análises exploratórias dos dados
**Variável de Destino**
<img src="https://user-images.githubusercontent.com/91911052/184802186-0ee4af5b-7742-4746-975a-24f8ccd83b45.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>


**Variável Numérica**
<img src="https://user-images.githubusercontent.com/91911052/184802297-479dab93-9760-4426-960b-7fae784c6d39.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://user-images.githubusercontent.com/91911052/184802348-e8eb1c01-9e74-42cb-878b-3d96f5569563.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

**Variável Categórica**
<img src="https://user-images.githubusercontent.com/91911052/184802417-1cb0b321-29a5-49d1-af72-b6637a8c9d54.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## Insights de negócio

* **H1**. Os 10 bairros com mais imóveis em São Paulo, seguem a mesma ordem nos somatório dos preços dos imóveis.

**FALSO**: Observamos que há uns maiores que os outros como **Brooklin Paulista** que é o 2º com mais imóveis atrás nos somatórios de preços de **Cidade Jardim** que é o 3º com mais imóveis. **Indicamos que o bairro de Brooklin Paulista pode ser uma opção mais fácil de compra de imóvel por ser o 2º bairro com mais imóveis em São Paulo e os preços mais baixos(somatório)**.
<img src="https://user-images.githubusercontent.com/91911052/184802886-37416d7e-3259-4c2f-9f57-feaff033d060.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H2**. Os 10 bairros com mais imóveis em São Paulo seguem a mesma ordem no número de vagas e quartos nos imóveis de acordo com suas metragens.

**VERDADEIRO**: Observamos que todos os 10 bairros possuem similaridade quanto a ordem de vagas, quartos e metragens.

<img src="https://user-images.githubusercontent.com/91911052/184803043-857ae6de-be13-4ccd-a26b-7a4f6930a21d.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H3**.Os 10 bairros com mais imóveis em São Paulo seguem a mesma ordem na faixa das metragens e preços/m² dos imóveis.

**FALSO**: Observamos que há faixas de metragens maiores ou menores que outros e não seguem a mesma ordem da quantidade de imóveis por bairro. **Cidade Jardim** e **Jardim Guedala**  são os que possuem as faixas de maiores metragens. **Para pessoas que procuram conforto em relação ao tamanho do imóvel, procurem nos bairros Cidade Jardim ou Jardim Guedala que é onde possuem faixa de preços similares aos outros e metragens maiores**.

<img src="https://user-images.githubusercontent.com/91911052/184803204-e9358403-97d2-4a06-8659-5c92275f6a1a.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H4**. A maioria das médias de pessoas com rendimento nominal médio mensal baixo, possui imóvel com valor de m² baixo também.

**VERDADEIRO**: Observamos que a maioria das médias de pessoas entre a faixa 0 e 20000 reais de renda média possuem imóveis com preço de m² entre 0 e 20000 reais, ou seja, baixo também. Alguns com renda baixa possuem imóveis com preço do m² mais caro e outros com renda alta, mas com imóveis com preço do m² mais barato, talvez por causa do bairro ou por opção mesmo. **Alertamos que pessoas com rendas mais baixas, não adquiram imóveis com valores muito altos como observamos no gráfico em algumas situações**.

<img src="https://user-images.githubusercontent.com/91911052/184803381-108d89f7-bc5d-4363-9467-91e98e979350.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 6 Machine Learning

Usamos alguns modelos de Machine Learning de regressão com o objetivo de obter a melhor acurácia e o menor número de erros possíveis.Como observado, o modelo **Randon Forest Regressor** foi o que teve o melhor resultado do **RMSE(1.497.535)** dentre todos usados, com os valores bem melhores como a acurácia(R2_Score), erro médio absoluto(MAE), raiz quadrada do erro médio(RMSE) e a média percentual absoluta do erro(MAPE), logo o utilizamos para obter resultados mais precisos no modelo final.

<img src="https://user-images.githubusercontent.com/91911052/184805470-c5cc4fbf-3402-4813-9c2d-fc4cb4876a75.jpg" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## 6.1 Resultados para o negócio

Esse projeto visa avaliar quanto vale um determinado imóvel na cidade de São Paulo que é usado como garantia de um empréstimo feito por um cliente na empresa **Creditas** .Após todas as análises exploratórias dos dados de imóveis de São Paulo e aplicações de modelos de Machine Learning, conseguimos obter as predições desses mesmos dados com uma boa acurácia e baixo erro. Com esses valores obtidos podemos estimar aproximadamente quanto a empresa **Creditas** vai poder emprestar à um possível cliente que deseje ter acesso a esse empréstimo no melhor e pior cenário.

<img src="https://user-images.githubusercontent.com/91911052/184809619-7304973d-f170-4c79-89c6-f02dd3d7df9d.jpg" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## 6.2 Desempenho de Machine Learning

O modelo usado foi o **Randon Forest Regressor** e os resultados obtidos foram esses abaixo:

|Modelo                  | MAE                  | MAPE                |f1-RMSE               | R2_Score AUC       |  
:----------------------- | :--------------------| :------------------ | :--------------------| :------------------| 
|Randon Forest Regressor | 751199.039667        | 0.301615            | 1.571333e+06         |0.776442            |

* Nesse prmeiro gráfico podemos observar os dados não completamente iguais, com algumas diferenças, mas com uma certa similaridade entre os valores reais e as predições.

<img src="https://user-images.githubusercontent.com/91911052/184807299-db343334-609f-44de-a957-33ea3f301057.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* Nesse segundo gráfico observamos a taxa de erro de cada valor de anúncio. Alguns poucos valores das predições 4 vezes maiores que o valor real de anúncio, mas em geral estão todos bem próximos um do outro(próximos de 1).

<img src="https://user-images.githubusercontent.com/91911052/184807345-98dfdd3c-7dac-4ff0-97a4-2a47e06d221d.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* Nesse terceiro gráfico podemos observar as dispersões entre valor real e predições, no qual podemos notar que há uma boa correlação entre os 2 dados.

<img src="https://user-images.githubusercontent.com/91911052/184807410-982ce98e-f6b9-4703-83bb-b552b8ed1400.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>
