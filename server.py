from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    url = f'{path}'
    headers = {key: value for (key, value) in request.headers if key != 'Host'}

    # Encaminha a solicitação para o endpoint de destino
    resposta_destino = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )

    # Cria uma resposta para o cliente com os dados recebidos do endpoint de destino
    resposta = Response(response=resposta_destino.content,
                        status=resposta_destino.status_code,
                        headers=resposta_destino.headers.items())

    return resposta


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
