from __main__ import app
from flask_mysqldb import MySQL

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' #Insira aqui a senha do seu servidor local do MYSQL
app.config['MYSQL_DB'] = 'usuarios'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



def insereUsuario(form):
    cur = mysql.connection.cursor()
    cur.execute(f" INSERT INTO usuarios(email_usuario, nome_usuario, descricao_usuario) VALUES(%s, %s, %s)", (form['email'], form['nome'], form['descricao']))
    mysql.connection.commit()
    cur.close()
    return None

def pegaUsuario():
    cur = mysql.connection.cursor()
    cur.execute(f" SELECT * FROM usuarios ")
    usuarios = cur.fetchall()
    cur.close()
    return usuarios