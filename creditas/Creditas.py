import pickle
import pandas as pd
import numpy as np
import math


class Creditas(object):
    def __init__(self):
        self.Robust_scaler = pickle.load(
            open("models/Robust_scaler.pkl", "rb")
        )

    def data_cleaning(self, df1):
        ##2.4 Formatação dos dados


        # Excluindo colunas com valores únicos
        df1.drop(
            [
                "cidade",
                "cod_grandes_regioes",
                "nome_grande_regiao",
                "cod_uf",
                "nome_da_uf ",
                "cod_meso",
                "nome_da_meso",
                "cod_micro",
                "nome_da_micro",
                "cod_rm",
                "nome_da_rm",
                "cod_municipio",
                "nome_do_municipio",
                "cod_bairro",
                "nome_do_bairro",
            ],
            axis=1,
            inplace=True,
        )

        # Excluindo colunas que se repetem
        df1.drop(
            ["cod_setor", "cod_distrito", "cod_subdistrito", "nome_do_subdistrito"],
            axis=1,
            inplace=True,
        )

        # Excluindo colunas que ja foram utilizadas e se tornaram inúteis
        df1.drop(["rua1", "latitude", "longitude", "point"], axis=1, inplace=True)

        # Retirar notação científica do 'setor_censo' para deixa-lo mais legível
        df1["setor_censo"] = df1[["setor_censo"]] / 1000000000

        ## 2.5 Checando e Tratando os dados vazios

        # Hipótese: Se é NA, talvez seja pela falta de informação dos locais
        # O que foi feito: A melhor solução encontrada foi pegar a moda das variáveis vazias por BAIRRO e preencher os dados que estão vazios
        # ja que os valores de cada bairro são semelhantes
        df1["mode1"] = (
            df1["bairro"]
            .apply(
                lambda x: df1[["setor_censo"]]
                .loc[df1["bairro"] == x, "setor_censo"]
                .mode()
                .values
            )
            .str[0]
        )
        df1["setor_censo"] = df1.apply(
            lambda x: x["mode1"] if math.isnan(x["setor_censo"]) else x["setor_censo"],
            axis=1,
        )

        df1["mode2"] = (
            df1["bairro"]
            .apply(
                lambda x: df1[["nome_do_distrito"]]
                .loc[df1["bairro"] == x, "nome_do_distrito"]
                .mode()
                .values
            )
            .str[0]
        )
        df1["nome_do_distrito"] = df1.apply(
            lambda x: x["mode2"]
            if pd.isnull(x["nome_do_distrito"])
            else x["nome_do_distrito"],
            axis=1,
        )

        df1["mode3"] = (
            df1["bairro"]
            .apply(
                lambda x: df1[["situacao_setor"]]
                .loc[df1["bairro"] == x, "situacao_setor"]
                .mode()
                .values
            )
            .str[0]
        )
        df1["situacao_setor"] = df1.apply(
            lambda x: x["mode3"]
            if math.isnan(x["situacao_setor"])
            else x["situacao_setor"],
            axis=1,
        )

        df1["mode4"] = (
            df1["bairro"]
            .apply(
                lambda x: df1[["tipo_setor"]]
                .loc[df1["bairro"] == x, "tipo_setor"]
                .mode()
                .values
            )
            .str[0]
        )
        df1["tipo_setor"] = df1.apply(
            lambda x: x["mode4"] if math.isnan(x["tipo_setor"]) else x["tipo_setor"],
            axis=1,
        )

        # Mesma idéia da solução acima, apenas trocando a MODA pela MÉDIA ja que são variáveis contínuas
        df1[
            [
                "mean1",
                "mean2",
                "mean3",
                "mean4",
                "mean5",
                "mean6",
                "mean7",
                "mean8",
                "mean9",
                "mean10",
                "mean11",
                "mean12",
            ]
        ] = df1["bairro"].apply(
            lambda x: df1[
                [
                    "v001",
                    "v002",
                    "v003",
                    "v004",
                    "v005",
                    "v006",
                    "v007",
                    "v008",
                    "v009",
                    "v010",
                    "v011",
                    "v012",
                ]
            ]
            .loc[
                df1["bairro"] == x,
                [
                    "v001",
                    "v002",
                    "v003",
                    "v004",
                    "v005",
                    "v006",
                    "v007",
                    "v008",
                    "v009",
                    "v010",
                    "v011",
                    "v012",
                ],
            ]
            .mean()
        )

        df1["v001"] = df1.apply(
            lambda x: x["mean1"] if math.isnan(x["v001"]) else x["v001"], axis=1
        )

        df1["v002"] = df1.apply(
            lambda x: x["mean2"] if math.isnan(x["v002"]) else x["v002"], axis=1
        )

        df1["v003"] = df1.apply(
            lambda x: x["mean3"] if math.isnan(x["v003"]) else x["v003"], axis=1
        )

        df1["v004"] = df1.apply(
            lambda x: x["mean4"] if math.isnan(x["v004"]) else x["v004"], axis=1
        )

        df1["v005"] = df1.apply(
            lambda x: x["mean5"] if math.isnan(x["v005"]) else x["v005"], axis=1
        )

        df1["v006"] = df1.apply(
            lambda x: x["mean6"] if math.isnan(x["v006"]) else x["v006"], axis=1
        )

        df1["v007"] = df1.apply(
            lambda x: x["mean7"] if math.isnan(x["v007"]) else x["v007"], axis=1
        )

        df1["v008"] = df1.apply(
            lambda x: x["mean8"] if math.isnan(x["v008"]) else x["v008"], axis=1
        )

        df1["v009"] = df1.apply(
            lambda x: x["mean9"] if math.isnan(x["v009"]) else x["v009"], axis=1
        )

        df1["v010"] = df1.apply(
            lambda x: x["mean10"] if math.isnan(x["v010"]) else x["v010"], axis=1
        )

        df1["v011"] = df1.apply(
            lambda x: x["mean11"] if math.isnan(x["v011"]) else x["v011"], axis=1
        )

        df1["v012"] = df1.apply(
            lambda x: x["mean12"] if math.isnan(x["v012"]) else x["v012"], axis=1
        )

        df1.drop(
            [
                "mode1",
                "mode2",
                "mode3",
                "mode4",
                "mean1",
                "mean2",
                "mean3",
                "mean4",
                "mean5",
                "mean6",
                "mean7",
                "mean8",
                "mean9",
                "mean10",
                "mean11",
                "mean12",
            ],
            axis=1,
            inplace=True,
        )

        # Hipótese: Se é NA, talvez seja pela falta de informação dos locais, pois são determinados bairros completamente sem informações em determinadas variáveis,
        # logo, não podemos achar moda, media ou mediana
        # O que foi feito:Apagaremos as outras 23 linhas ja que são bairros completamente sem informações e não conseguimos achar uma solução para elas
        df1 = df1.dropna()

        ## 2.6 Alterando os Tipos de Dados¶

        a = pd.CategoricalDtype(
            categories=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ordered=True
        )
        df1["quartos"] = df1["quartos"].astype(a)

        b = pd.CategoricalDtype(
            categories=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14], ordered=True
        )
        df1["banheiros"] = df1["banheiros"].astype(b)

        c = pd.CategoricalDtype(
            categories=[
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                20,
                24,
                25,
                30,
                38,
            ],
            ordered=True,
        )
        df1["vagas"] = df1["vagas"].astype(c)

        df1["cep"] = df1["cep"].astype(str)

        df1["setor_censo"] = df1["setor_censo"].astype(str)

        d = pd.CategoricalDtype(categories=[1.0, 2.0, 3.0, 4.0, 8.0], ordered=True)
        df1["situacao_setor"] = df1["situacao_setor"].astype(d)

        e = pd.CategoricalDtype(categories=[0.0, 1.0], ordered=True)
        df1["tipo_setor"] = df1["tipo_setor"].astype(e)

        return df1

    def feature_engineering(self, df2):
        # 4 Filtrando o quadro de dados

        # Substituindo outlierss
        df2["valor_anuncio"] = df2["valor_anuncio"].apply(
            lambda x: 30000000 if (x > 30000000) else x
        )

        df2["metragem"] = df2["metragem"].apply(lambda x: 2850 if (x > 10000) else x)

        df2["v004"] = df2["v004"].apply(lambda x: 5.52 if (x > 6) else x)

        df2["v006"] = df2["v006"].apply(
            lambda x: 1781723643.14 if (x > 2000000000) else x
        )

        df2["v008"] = df2["v008"].apply(
            lambda x: 1374996829.42 if (x > 1500000000) else x
        )

        df2["v010"] = df2["v010"].apply(
            lambda x: 976628790.68 if (x > 1000000000) else x
        )

        df2["v012"] = df2["v012"].apply(
            lambda x: 1436259424.69 if (x > 1500000000) else x
        )

        df3 = df2.copy()

        ## 4.6 Engenharia de Recursos

        # sub regioes
        df3["sub_regiões"] = df3["cep"].str.extract("([0-9])")
        df3["sub_regiões"] = df3["sub_regiões"].astype(str)

        # setor
        df3["setor"] = df3["cep"].str[1]
        df3["setor"] = df3["setor"].astype(str)

        # sub setor
        df3["sub_setor"] = df3["cep"].str[2]
        df3["sub_setor"] = df3["sub_setor"].astype(str)

        # divisao sub setor
        df3["divisao_sub_setor"] = df3["cep"].str[3]
        df3["divisao_sub_setor"] = df3["divisao_sub_setor"].astype(str)

        # quant_dom_part
        df3["quant_dom_part"] = ""
        for idx, _ in df3.iterrows():
            if df3["v001"].at[idx] < 100:
                df3["quant_dom_part"].at[idx] = "Pouco domicílio"
            elif (df3["v001"].at[idx] >= 100) & (df3["v001"].at[idx] < 200):
                df3["quant_dom_part"].at[idx] = "Médio 1 domicílio"
            elif (df3["v001"].at[idx] >= 200) & (df3["v001"].at[idx] < 350):
                df3["quant_dom_part"].at[idx] = "Médio 2 domicílio"
            else:
                df3["quant_dom_part"].at[idx] = "Muito domicílio"

        # quant_mor
        df3["quant_mor"] = ""
        for idx, _ in df3.iterrows():
            if df3["v002"].at[idx] < 200:
                df3["quant_mor"].at[idx] = "Pouco morador"
            elif (df3["v002"].at[idx] >= 200) & (df3["v002"].at[idx] < 400):
                df3["quant_mor"].at[idx] = "Médio 1 morador"
            elif (df3["v002"].at[idx] >= 400) & (df3["v002"].at[idx] < 600):
                df3["quant_mor"].at[idx] = "Médio 2 morador"
            else:
                df3["quant_mor"].at[idx] = "Muito morador"

        return df3

    def atributo_frequencia(self, atributo):
        # Cria um dicionário de valores contáveis
        atributo_dict = atributo.value_counts().to_dict()

        # Armazena valores com Dataframe
        df_atributo_dict = pd.DataFrame(
            atributo_dict.items(), columns=["Value", "Count"]
        )

        # Calcula a frequência de cada valor
        df_atributo_dict["frequency"] = (
            df_atributo_dict["Count"] / df_atributo_dict["Count"].sum()
        )

        # Obtém um dicionário para a frequência
        atributo_frequencia = df_atributo_dict.set_index("Value").to_dict()["frequency"]

        return atributo_frequencia

    def frequencias_codificadas(self, data_frame):
        # Cria um Dataframe vazio
        freq_codificada = pd.DataFrame()

        # Cria colunas de frequências
        for column in data_frame.columns:
            freq_codificada[column] = data_frame[column].map(
                self.atributo_frequencia(data_frame[column])
            )

        return freq_codificada

    def data_preparation(self, df5):
        categorical = df5[
            [
                "bairro",
                "quartos",
                "banheiros",
                "vagas",
                "rua",
                "cep",
                "setor_censo",
                "nome_do_distrito",
                "sub_regiões",
                "setor",
                "sub_setor",
                "divisao_sub_setor",
                "quant_dom_part",
                "quant_mor",
            ]
        ].copy()
        numerical = df5[
            [
                "metragem",
                "valor_anuncio",
                "valor_mm",
                "valor_m2",
                "v001",
                "v002",
                "v003",
                "v004",
                "v005",
                "v006",
                "v007",
                "v008",
                "v009",
                "v010",
                "v011",
                "v012",
            ]
        ].copy()
        binary = df5[["situacao_setor", "tipo_setor"]].copy()

        Alvo_var = df5[["valor_anuncio"]].copy()
        Alvo_var["valor_anuncio"] = np.log1p(Alvo_var["valor_anuncio"])

        numerical.drop(columns=["valor_anuncio"], inplace=True)

        numerical_1 = self.Robust_scaler.fit_transform(numerical[["metragem","valor_mm","valor_m2","v001","v002","v003",
                                                                  "v004","v005","v006","v007","v008","v009",
                                                                  "v010","v011","v012",]].values)
        numerical_2 = pd.DataFrame(
            numerical_1,
            columns=numerical[
                [
                    "metragem",
                    "valor_mm",
                    "valor_m2",
                    "v001",
                    "v002",
                    "v003",
                    "v004",
                    "v005",
                    "v006",
                    "v007",
                    "v008",
                    "v009",
                    "v010",
                    "v011",
                    "v012",
                ]
            ].columns,
        )

        categorical_2 = self.frequencias_codificadas(categorical)

        df6 = pd.concat([binary, numerical_2, categorical_2, Alvo_var], axis=1)
        df6 = df6.astype(float)
        df6 = df6[
            [
                "metragem",
                "vagas",
                "banheiros",
                "bairro",
                "quartos",
                "v011",
                "v007",
                "v005",
                "v009",
                "nome_do_distrito",
                "cep",
                "rua",
                "setor_censo",
                "setor",
                "divisao_sub_setor",
                "v003",
                "sub_regiões",
                "v004",
            ]
        ]

        return df6

    def get_prediction(self, model, original_data, test_data):
        # predição
        pred = model.predict(test_data)
        original_data["predição"] = np.expm1(pred)

        return original_data
