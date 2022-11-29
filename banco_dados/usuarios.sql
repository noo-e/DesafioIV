CREATE DATABASE usuarios;
USE usuarios;
CREATE TABLE usuarios(
	id_usuario int PRIMARY KEY AUTO_INCREMENT,
	email_usuario varchar(50),
    nome_usuario varchar(50),
    descricao_usuario varchar(50));