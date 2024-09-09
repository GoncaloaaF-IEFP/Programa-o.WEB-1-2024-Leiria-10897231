from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/homepage')
def index():
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



@app.route('/template2')
def template2():
    return render_template("pag2.html",
                           titulo = "Pagina 2",
                           header = "a minha 2ª pagina Flask com dados ..."
                           )

@app.route('/template3')
def template3():
    return render_template("pag2.html",
                           titulo = "Pagina 3",
                           header = "Pagina 3"
                           )


@app.route('/template4/<nome>')
def template4(nome:str):
    return render_template("pag2.html",
                           titulo = "Pagina 4",
                           header = f"Temp4: Bem Vindo, {nome}"
                           )

@app.route('/template5/')
def template5():
    nome = request.args.get('nome')
    return render_template("pag2.html",
                           titulo = "Pagina 5",
                           header = f"Temp5: Bem Vindo, {nome}"
                           )


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("not_found.html"), 404





