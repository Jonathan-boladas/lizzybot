import requests
from flask import Flask
from urllib.parse import urlencode

app = Flask(__name__)

TOKEN = 'COLOQUE_SEU_TOKEN_AQUI'
CHAT_ID = '6874195565'

@app.route('/', methods=['GET'])
def home():
    return 'Lizzy Bot Online!'

@app.route('/ligar', methods=['GET'])
def ligar():
    texto = "Robô Lizzy foi <b>LIGADO</b> com sucesso!"
    params = {'chat_id': CHAT_ID, 'text': texto, 'parse_mode': 'HTML'}
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?' + urlencode(params)
    requests.get(url)
    return 'Comando LIGAR enviado'

@app.route('/desligar', methods=['GET'])
def desligar():
    texto = "Robô Lizzy foi <b>DESLIGADO</b> com sucesso!"
    params = {'chat_id': CHAT_ID, 'text': texto, 'parse_mode': 'HTML'}
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?' + urlencode(params)
    requests.get(url)
    return 'Comando DESLIGAR enviado'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
  add main code
