from flask import Flask, jsonify, request

app = Flask(__name__)

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

# Consultar(todos)
@app.route('/noticias',methods=['GET'])
def ler_noticia():
    return jsonify(noticias)
# Consultar(id)
@app.route('/noticias/<int:id>',methods=['GET'])
def ler_noticia_por_id(id):
    for noticia in noticias:
        if noticia.get("id") == id:
            return jsonify(noticia) 
# Editar
@app.route('/noticias/<int:id>',methods=['PUT'])
def editar_noticia_por_id(id):
    noticia_alterada = request.get_json()
    for indice,noticia in enumerate(noticias):
        if noticia.get('id') == id:
            noticias[indice].update(noticia_alterada)
            return jsonify(noticias[indice])
# Criar
@app.route('/noticias',methods=['POST'])
def incluir_nova_noticia(id):
    nova_noticia = request.get_json()
    noticias.append(nova_noticia)

    return jsonify(noticias)
# Excluir
@app.route('/noticias/<int:id>',methods=['DELETE'])
def excluir_noticia(id):
    for indice, noticia in enumerate(noticias):
        if noticia.get('id') == id:
            del noticias[indice]
    
    return jsonify(noticias)
    
app.run(port = 5000, host = 'localhost', debug = True)