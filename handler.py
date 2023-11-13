import os
import json
import pickle
import pandas as pd
from flask import Flask, request, Response
from creditas.Creditas import Creditas

# loading model
model = pickle.load(open("models/modelo_final.pkl", "rb"))


def creditas_predict(data):
    data = pd.DataFrame( data )

    # Instantiate Rossmann class
    pipeline = Creditas()

    # data cleaning
    df1 = pipeline.data_cleaning(data)

    # feature engineering
    df2 = pipeline.feature_engineering(df1)

    # data preparation
    df3 = pipeline.data_preparation(df2)

    # prediction
    df_response = pipeline.get_prediction(model, data, df3)

    return df_response
