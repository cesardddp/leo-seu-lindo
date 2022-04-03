from flask import Flask
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.get("/")
def index():
    response = requests.get(
        "https://precodoscombustiveis.com.br/pt-br/station/brasil/sao-paulo/rio-claro/district/comercial-de-combustiveis-apollo-rio-claro-ltda/25091"
    )
    return response.text

app.run()