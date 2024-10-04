from flask import Flask, jsonify, request
from flask_swagger_ui import swaggerui_blueprint
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app=app, version='1.0', title='Notícias API')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

# Configurar o Swagger UI
swaggerui_blueprint = swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Notícias API",
        'title': "Notícias API",
        'version': "1.0"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

required_fields = ['titulo', 'corpo', 'autor']

noticias = [
    {
        'id': 1,
        'titulo': 'Reciclável',
        'corpo': 'Materiais',
        'autor': 'Paulo',
        'data_criacao': 2024
    },
    {
        'id': 2,
        'titulo': 'Chaves',
        'corpo': 'Chaves misteriosas',
        'autor': 'Marlene',
        'data_criacao': 2023
    },
    {
        'id': 3,
        'titulo': 'Gavetas',
        'corpo': 'Gavetas abertas',
        'autor': 'João',
        'data_criacao': 2021
    }
]

# Rotas da API
@app.route('/news', methods=['GET'])
def listar_noticias():
    return jsonify(noticias)

@app.route('/news/<int:id>', methods=['GET'])
def obter_noticia(id):
    noticia = next((n for n in noticias if n['id'] == id), None)
    if noticia:
        return jsonify(noticia)
    return jsonify({'message': 'Notícia não encontrada'}), 404

@app.route('/news', methods=['POST'])
def criar_nova_noticia():
    dados = request.json
    if not dados:
        return jsonify({"error": "Dados vazios"}), 400
    
    for field in required_fields:
        if field not in dados:
            return jsonify({f"error": f"{field} não encontrado"}), 400
    
    nova_noticia = {
        'id': len(noticias) + 1,
        'titulo': dados.get('titulo'),
        'corpo': dados.get('corpo'),
        'autor': dados.get('autor'),
        'data_criacao': str(dados.get('data_criacao', 'N/A'))
    }
    noticias.append(nova_noticia)
    return jsonify(nova_noticia), 201

@app.route('/news/<int:id>', methods=['PUT'])
def atualizar_noticia(id):
    noticia = next((n for n in noticias if n['id'] == id), None)
    if noticia:
        dados = request.json
        if not dados:
            return jsonify({"error": "Dados vazios"}), 400
        
        for field in required_fields:
            if field not in dados:
                return jsonify({f"error": f"{field} não encontrado"}), 400
        
        noticia.update({
            'titulo': dados.get('titulo', noticia['titulo']),
            'corpo': dados.get('corpo', noticia['corpo']),
            'autor': dados.get('autor', noticia['autor']),
            'data_criacao': str(dados.get('data_criacao', noticia['data_criacao']))
        })
        return jsonify(noticia), 200
    return jsonify({'message': 'Notícia não encontrada'}), 404

@app.route('/news/<int:id>', methods=['DELETE'])
def deletar_noticia(id):
    noticias = [n for n in noticias if n['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=False)