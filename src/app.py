from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import conexao

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Meusequel@d0' #Insira aqui a senha do seu servidor local do MYSQL
app.config['MYSQL_DB'] = 'usuarios'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

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

if __name__ == '__main__':
    app.run(debug = True)