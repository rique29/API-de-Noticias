from flask import Flask, jsonify, request
from flask_swagger_ui import swaggerui_blueprint
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app=app, version='1.0', title='Notícias API')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Configurações do Swagger UI
        'app_name': "Notícias API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

required_fields = ['titulo', 'corpo', 'autor']

noticias = [
    {
        'id': 1,
        'titulo': 'Reciclavel',
        'Corpo_da_noticia': 'materiais',
        'Autor': 'Paulo',
        'Data_de_Criação': 2024
    },
    {
        'id': 2,
        'titulo': 'Chaves',
        'Corpo_da_noticia': 'chaves misteriosas',
        'Autor': 'Marlene',
        'Data_de_Criação': 2023
    },
    {
        'id': 3,
        'titulo': 'Gavetas',
        'Corpo_da_noticia': 'gavetas abertas',
        'Autor': 'João',
        'Data_de_Criação': 2021
    }
]

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
        'titulo': dados['titulo'],
        'corpo': dados['corpo'],
        'autor': dados['autor'],
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
        
        noticia['titulo'] = dados.get('titulo', noticia['titulo'])
        noticia['corpo'] = dados.get('corpo', noticia['corpo'])
        noticia['autor'] = dados.get('autor', noticia['autor'])
        noticia['data_criacao'] = str(dados.get('data_criacao', noticia['data_criacao']))
        return jsonify(noticia)
    return jsonify({'message': 'Notícia não encontrada'}), 404

@app.route('/news/<int:id>', methods=['DELETE'])
def deletar_noticia(id):
    noticias = [n for n in noticias if n['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)