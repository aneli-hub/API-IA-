from flask import Flask, request, render_template, redirect

# salvar CSV
import csv, os

app = Flask(__name__)

ARQUIVO = 'dados.csv'

# criar o arquivo csv cao ele exista
def inicializar_csv():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w', newline="", encoding="UTF-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Nome", "Email", "Produto", "Quantidade"])

# ler os registros do sistema 
def ler_registros():
    inicializar_csv()
    with open(ARQUIVO, 'r', newline="", encoding="UTF-8")as arquivo:
        reader = csv.reader(arquivo)
        return list(reader)
    
    
@app.route("/", methods=["GET", "POST"])
def index():
    
    
   # se for o metodo Post a pessoa vai criar algo

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        produto = request.form["produto"]
        quantidade = request.form["quantidade"]
    
        with open(ARQUIVO, 'a', newline="", encoding="UTF-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([nome, email, produto, quantidade])

    #Get
    registros = ler_registros()
    return render_template("index.html", registros=registros)

if __name__ == "__main__":
    inicializar_csv()
    app.run(debug=True)