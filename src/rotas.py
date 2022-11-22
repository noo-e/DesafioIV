from __main__ import app
from flask import Flask, render_template, request
import conexao

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        form = request.form
        conexao.insereUsuario(form)
        return render_template('contato.html')
    else:
        return render_template('contato.html')

@app.route('/quem-somos')
def quemSomos():
    return render_template('quem-somos.html')

@app.route('/usuarios')
def usuarios():
    usuarios = conexao.pegaUsuario()
    return render_template('usuarios.html', usuarios = usuarios)