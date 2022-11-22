from app import mysql



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