from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/pag2')
def pag2():
    return 'Hello World!- pag 2'

@app.route('/pag3/')
def pag3():
    return f"Hello World, Desconhecido"

@app.route('/pag3/<nome>')
def pag3_nome(nome:str):
    return f"Hello World, {nome}"


'''

?nome=Gonçalo&ano=2024
http://127.0.0.1:5000/pag4?nome=Gonçalo&ano=2024

'''
@app.route('/pag4')
def pag3_dados():
    print(request.query_string)
    ano = request.args.get('ano')
    nome = request.args.get('nome')
    return f"Hello World, {nome}, {ano}"


@app.route('/template')
def template():
    return render_template("pag1.html")


