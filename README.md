# Alura_Creditas
Projeto de regressão com objetivo de obter predições de valores de imóveis da cidade de São Paulo.

<div align="center">
<img src="https://user-images.githubusercontent.com/91911052/184797458-b67d17bd-d04f-4fb5-bfa0-79617cb8a3b9.jpg" width="700px" />
</div>

# 1 Sobre a Creditas
O brasileiro tem fácil acesso às piores taxas de juros, e a Creditas nasceu para mudar essa realidade. Eles combatem o mau endividamento com um crédito de qualidade, que permite que os bens levem ainda mais longe. O objetivo é garantir o seu progresso financeiro e ajudar a realizar projetos de vida. Fintech criada em 2012, a Creditas é especialista em empréstimos com imóvel ou carro como garantia; empresa já emprestou R$ 300 milhões no Brasil e tem 370 funcionários.

# 2 Apresentação
Nesse projeto proposto pela Alura, obtive um modelo de Regressão com o objetivo de predizer quanto vale um determinado imóvel na cidade de São Paulo que é usado como garantia de um empréstimo feito por um cliente na empresa Creditas. A fim de obter valores mais próximos possíveis do real, fiz uma análise exploratória dos dados existentes de imóveis com várias informações para facilitar o entendimento do negócio e conseguir o objetivo final. O modelo foi colocado em produção no ambiente cloud do AWS, além da criação de um bot Telegram que é capaz de responder a pergunta **Quanto vale um determinado imóvel na cidade de São Paulo?**. O usúario coloca um ID pelo Telegram e o modelo responde com o valor da predição se esse ID existir.
- O robô pode ser acessado através desse link: <a href="https://t.me/creditas_tel_bot">TelegramBot</a> 
- Informações sobre a Creditas podem ser encontradas nesse link: <a href="https://www.creditas.com/quem-somos">siteCreditas</a>

O projeto completo pode ser encontrado neste link:
<a href="https://github.com/hugoferraz5/Alura_Creditas2/blob/main/Creditas_alura1.ipynb">ProjetoAlura</a>

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
* **Deploy** - Através do cloud da AWS, implantamos o nosso modelo de Machine Learning e esse modelo responderá requisições via API por meio do Telegram Bot.
<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/3367ccbc-fcf0-43a6-9f4c-395eb9c0192c.png" alt="pic1" style="zoom:55% ;" />

# 5 Análises exploratórias dos dados
**Variável de Destino**
<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/5b4ca46d-95da-40fe-884b-fa15131ac984.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>


**Variável Numérica**
<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/5f027ef2-27cf-43d0-98a5-a29472100ae6.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/6fcd77a1-1a73-4096-ba46-565f8fa4309c.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

**Variável Categórica**
<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/f13f2156-d9bc-4d04-a813-0ca989665f7d.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## Insights de negócio

* **H1**. Os 10 bairros com mais imóveis em São Paulo, seguem a mesma ordem nos somatório dos preços dos imóveis. 

**FALSO**: Observamos que há uns maiores que os outros como **Brooklin Paulista** que é o 2º com mais imóveis atrás nos somatórios de preços de **Cidade Jardim** que é o 3º com mais imóveis. **Indicamos que o bairro de Brooklin Paulista pode ser uma opção mais fácil de compra de imóvel por ser o 2º bairro com mais imóveis em São Paulo e os preços mais baixos(somatório)**.
<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/5e145557-9645-4242-a13a-b93a519910fd.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/fa86e17e-5ff5-4863-9e5a-f1aeed8f4d48.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H2**. Os 10 bairros com mais imóveis em São Paulo seguem a mesma ordem no número de vagas e quartos nos imóveis de acordo com suas metragens.

**VERDADEIRO**: Observamos que todos os 10 bairros possuem similaridade quanto a ordem de vagas, quartos e metragens.

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/1e237b92-c16a-44ee-93a9-4b0fbe1789c6.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H3**.Os 10 bairros com mais imóveis em São Paulo seguem a mesma ordem na faixa das metragens e preços/m² dos imóveis.

**FALSO**: Observamos que há faixas de metragens maiores ou menores que outros e não seguem a mesma ordem da quantidade de imóveis por bairro. **Cidade Jardim** e **Jardim Guedala**  são os que possuem as faixas de maiores metragens. **Para pessoas que procuram conforto em relação ao tamanho do imóvel, procurem nos bairros Cidade Jardim ou Jardim Guedala que é onde possuem faixa de preços similares aos outros e metragens maiores**.

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/00a7a56d-e204-4d13-91ee-a1553da4b11a.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H4**. Os valores das médias apenas de pessoas com rendimento nominal médio mensal é diretamente proporcional ao valor do m² dos imóveis.

**VERDADEIRO**: A maioria dos imóveis possuem valor do m2 abaixo dos 20000 reais e estão localizados em áreas onde as médias de pessoas com rendimento nominal mensal é abaixo dos 20000 reais, ou seja, baixo também.A partir do momento que o valor do m2 sobe acima dos 20000 reais, a renda nominal média continua baixo, e a partir do momento que a renda nominal média fica acima dos 20000 reais, o valor do m2 continua baixo também , mostrado também na correlação que é menor que 0.5 e tudo isso, talvez por causa da aŕea localizada ou por opção das pessoas mesmo. **Pessoas com rendas mais baixas não precisam adquirir imóveis com valores muito altos como observamos no gráfico em algumas situações. Existem vários imóveis com valores/m2 abaixo dos 20000 reais e com atributos(metragem,quartos,banheiros e vagas) não tão diferentes dos imóveis de valores acima de 20000/m2**.

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/b54affa3-bc3e-4d60-a3c2-bbc87131929f.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/b3f3ba5c-303f-446f-af48-d2d3b84f3ff5.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/4a4a0603-2f69-4d4e-b111-9e0ae9e8fa15.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 6 Machine Learning

Usamos alguns modelos de Machine Learning de regressão com o objetivo de obter a melhor acurácia e o menor número de erros possíveis.Como observado, o modelo **Randon Forest Regressor** foi o que teve o melhor resultado do **RMSE(0.290553)** dentre todos usados, com os valores bem melhores como a acurácia(R2_Score), erro médio absoluto(MAE), raiz quadrada do erro médio(RMSE) e a média percentual absoluta do erro(MAPE), logo o utilizamos para obter resultados mais precisos no modelo final.

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/14dc854b-831b-4730-9dfe-6ea9894122d1.jpg" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## 6.1 Resultados para o negócio

Esse projeto visa avaliar quanto vale um determinado imóvel na cidade de São Paulo que é usado como garantia de um empréstimo feito por um cliente na empresa **Creditas** .Após todas as análises exploratórias dos dados de imóveis de São Paulo e aplicações de modelos de Machine Learning, conseguimos obter as predições desses mesmos dados com uma boa acurácia e baixo erro. Com esses valores obtidos podemos estimar aproximadamente quanto a empresa **Creditas** vai poder emprestar à um possível cliente que deseje ter acesso a esse empréstimo no melhor e pior cenário.

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/49893603-027c-42b6-91ba-c110f833df79.jpg" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## 6.2 Desempenho de Machine Learning

O modelo usado foi o **Randon Forest Regressor** e os resultados obtidos foram esses abaixo:

|Modelo                  | MAE                  | MAPE                |f1-RMSE               | R2_Score AUC       |  
:----------------------- | :--------------------| :------------------ | :--------------------| :------------------| 
|Randon Forest Regressor | 0.242175             | 0.016765            | 0.322253             |0.874314            |

* Nesse prmeiro gráfico podemos observar os dados não completamente iguais, com algumas diferenças, mas com uma certa similaridade entre os valores reais e as predições.

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/7b22eaa2-f0e1-46a3-82b1-076def99028e.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* Nesse segundo gráfico observamos a taxa de erro de cada valor de anúncio. Alguns poucos valores das predições 4 vezes maiores que o valor real de anúncio, mas em geral estão todos bem próximos um do outro(próximos de 1).

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/b0116c4f-54f6-4a7e-90e3-026491c4e2ea.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* Nesse terceiro gráfico podemos observar as dispersões entre valor real e predições, no qual podemos notar que há uma boa correlação entre os 2 dados.

<img src="https://github.com/hugoferraz5/Alura_Creditas2/assets/91911052/71d2ed3c-301c-4943-a130-042ba74aac2c.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

# 7 Próximos passos

- Utilizar outros Modelos e Machine Learning para testar se os resultados podem ser ainda melhores.
- Melhorar as respostas do telgregam bot com implementação de gráficos.
- Adicionar mais Hipóteses para análise de dados.
- Melhorar as análises de dados com adições de gráficos mais claros.

# 8.0 - Ferramentas utilizadas

Manipulação e limpeza dos dados: pandas, numpy

VIsualização dos dados: matplotlib, seaborn

Machine learning: Regressão (scikit-learn e Random Forrest Regressor), selação de features (Boruta)

Ambiente Cloud: Flask, requests, Ngrok, desenho de API e AWS
