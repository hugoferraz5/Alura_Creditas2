import inflection
import json
import requests
import pandas as pd
import os
from flask import Flask, request, Response

# constants
data_path = '' #'/home/hugo/Hugo/Projetos/Projeto-SaoPaulo/Projeto/'

# Get about me
#https://api.telegram.org/bot6808034007:AAHBOUQNPU62qcPP6CyFvlZ-BesMANOeRGc/getMe

# Get updates
#https://api.telegram.org/bot6808034007:AAHBOUQNPU62qcPP6CyFvlZ-BesMANOeRGc/getUpdates

# Set webhook
#https://api.telegram.org/bot6808034007:AAHBOUQNPU62qcPP6CyFvlZ-BesMANOeRGc/setWebhook?url=https://0f82-54-91-48-217.ngrok-free.app/

def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(token)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)

    r = requests.post(url, json={'text':text} )
    print( 'Status code: {}'.format(r.status_code))

    return None

def parse_message(message):
    chat_id = message['message']['chat']['id']
    sales_id = message['message']['text']

    sales_id = sales_id.replace('/', '')

    try:
        sales_id = int(sales_id)
    
    except ValueError:
        sales_id = 'error'

    return chat_id, sales_id

def load_dataset(sales_id):
    ibge_sp = pd.read_csv(
        'https://gist.githubusercontent.com/tgcsantos/85f8c7b0a2edbc3e27fcad619b37d886/raw/a4954781e6bca9cb804062a3eea0b3b84679daf4/Basico_SP1.csv',
        encoding='ISO-8859-1',
        sep=';', thousands='.', decimal=','
        )
    ibge_sp.dropna(how='all', axis=1, inplace=True)
    data_geo = pd.read_csv("datasets/dados_geo.csv")

    data_vendas_censo = pd.merge(left = data_geo, right = ibge_sp, how = "left", left_on = "setor_censo", right_on = "Cod_setor")

    data_vendas_censo.rename(columns={'Rua':'rua1'},inplace=True)
    data_vendas_censo.rename(columns={'Cod_Grandes Regiï¿½es':'cod_grandes_regioes'},inplace=True)

    cols = tuple(map(lambda x: inflection.underscore(x), data_vendas_censo.columns))
    data_vendas_censo.columns = cols

    df_predict = data_vendas_censo.copy()
    df_predict = df_predict.head(30)

    # Choose store for prediction
    df_predict = df_predict.iloc[[sales_id]]

    if not df_predict.empty:
        # Convert test dataframe in json
        data = json.dumps(df_predict.to_dict(orient='records'))

    else:
        data = 'error'

    return data

def predict_sales(data):
    # API Call
    url = '0.0.0.0:5001/creditas/predict'
    header = {'Content-type': 'application/json'}
    #data = data

    r = requests.post(url, data=data, headers=header)
    print('Status Code {}'.format(r.status_code))

    d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())

    return d1

# API initialize
app = Flask(__name__)
token = '6808034007:AAHBOUQNPU62qcPP6CyFvlZ-BesMANOeRGc'

@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'POST':
        message = request.get_json()

        chat_id, sales_id = parse_message(message)

        if sales_id != 'error':
            #loading data
            data = load_dataset(sales_id)

            if data != 'error':
                #prediction
                d1 = predict_sales(data)
                #calculation
                for i in range(len(d1)):
    
                    message = 'O preço do imóvel {} selecionado é ${:,.2f}'.format(i,d1.loc[i, 'predição'])
                    
                #send message
                send_message(chat_id, message)
                return Response('Ok', status=200)
            else:
                send_message(chat_id, 'Property not available. Try another number')
                return Response('Ok', status=200)                

        else:
            send_message(chat_id, 'Insert the Sales ID to predict property prices in the city of São Paulo. You can enter the ID by sending /Sales ID or just the Sales ID number.')
            return Response('Ok', status=200)

    else:
        return "<h1> Hello, I am Credita's sales forecast bot, enter Sales ID to predict property prices in the city of São Paulo. <h1>"

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port, debug=True)