from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O esplêndido e o Vil',
        'autor': 'Erik Larson'
    },
    {
        'id': 2,
        'título': 'Breves respostas para Grandes questões',
        'autor': 'Stephen Hawking'
    },
    {
        'id': 3,
        'título': 'A História do Século XX',
        'autor': 'Martin Gilbert'
    },
]

# Consultar
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
             return jsonify(livro) 


# Editar

# Excluir
app.run(port=5000, host='localhost', debug=True)