# flask | festAPI

# pip install flask
from flask import Flask, request, render_template, jsonify

# criando a aplicação em flask
app = Flask(__name__)

# Rota de exemplo
@app.route('/helloworld', methods=['GET'])
def helloworld():
        return jsonify( {
           "msg": "Ola mundo!"    
               
            
  })
@app.route('/')
def home():
        return render_template('index.html', registros=registros)
# iniciar o servidor

if __name__ == '__main__':
        app.run(debug=True)