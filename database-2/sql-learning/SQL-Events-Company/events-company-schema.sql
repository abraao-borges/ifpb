CREATE TABLE evento (
	id serial PRIMARY KEY,
  	tipo varchar(50),
  	inicio timestamp,
 	termino timestamp
);

CREATE TABLE cliente (
	id serial PRIMARY KEY,
  	nome varchar(70),
  	id_cliente_evento integer,
  	CONSTRAINT cliente_evento_fk FOREIGN KEY (id_cliente_evento) REFERENCES evento(id) ON DELETE set null
);

CREATE TABLE convidado (
	id serial PRIMARY KEY,
  	nome varchar(70),
  	id_convidado_evento integer,
  	CONSTRAINT convidado_evento_fk FOREIGN KEY (id_convidado_evento) REFERENCES evento(id)
);

CREATE TABLE servico (
	id serial PRIMARY KEY,
  	tipo varchar(100),
  	id_servico_evento integer,
  	CONSTRAINT servico_evento_fk FOREIGN KEY (id_servico_evento) REFERENCES evento(id)
);

CREATE TABLE funcionario (
	id serial PRIMARY KEY,
  	nome varchar(50),
  	id_funcionario_evento integer,
  	CONSTRAINT funcionario_evento_fk FOREIGN KEY (id_funcionario_evento) REFERENCES evento(id)
);

CREATE TABLE local (
	id serial PRIMARY KEY,
  	nome varchar(100),
  	capacidade integer,
  	id_local_evento integer,
  	CONSTRAINT local_evento_fk FOREIGN KEY (id_local_evento) REFERENCES evento(id) ON DELETE set null
);

INSERT INTO evento(tipo, inicio, termino) values ('Aniversário Infantil', '2004-12-29 19:00:00', '2004-12-29 22:00:00');
INSERT INTO evento(tipo, inicio, termino) values ('Festa de Casamento', '2025-10-01 10:00:00', '2025-10-01 17:00:00');
INSERT INTO evento(tipo, inicio, termino) values ('Chá de Revelação', '2033-07-15 19:00:00', '2033-07-15 21:00:00');

INSERT INTO cliente(nome, id_cliente_evento) values ('Amaral de Souza', 1)
INSERT INTO cliente(nome, id_cliente_evento) values ('Roseane Carmo', 2)
INSERT INTO cliente(nome, id_cliente_evento) values ('Felicion Braga', 3)

INSERT INTO convidado(nome, id_convidado_evento) values ('Pedro', 1)
INSERT INTO convidado(nome, id_convidado_evento) values ('Gabriel', 1)
INSERT INTO convidado(nome, id_convidado_evento) values ('Felipe', 1)
INSERT INTO convidado(nome, id_convidado_evento) values ('Douglas', 2)
INSERT INTO convidado(nome, id_convidado_evento) values ('Carlos', 2)
INSERT INTO convidado(nome, id_convidado_evento) values ('Jeferson', 2)
INSERT INTO convidado(nome, id_convidado_evento) values ('Maria', 3)
INSERT INTO convidado(nome, id_convidado_evento) values ('Ana', 3)
INSERT INTO convidado(nome, id_convidado_evento) values ('Rafaela', 3)

INSERT INTO servico(tipo, id_servico_evento) values ('Bolo e Salgadinhos', 1)
INSERT INTO servico(tipo, id_servico_evento) values ('Cama elástica e outros brinquedos', 1)
INSERT INTO servico(tipo, id_servico_evento) values ('Bufê completo + bolo', 2)
INSERT INTO servico(tipo, id_servico_evento) values ('Maquiagem da noiva', 2)
INSERT INTO servico(tipo, id_servico_evento) values ('Enfeitos cor de rosa e cor azul', 3)
INSERT INTO servico(tipo, id_servico_evento) values ('Balão com tinta rosa (não deixe o cliente saber)', 3)

INSERT INTO funcionario(nome, id_funcionario_evento) values ('Angela', 1)
INSERT INTO funcionario(nome, id_funcionario_evento) values ('Antonio', 1)
INSERT INTO funcionario(nome, id_funcionario_evento) values ('Daniel', 2)
INSERT INTO funcionario(nome, id_funcionario_evento) values ('Pamela', 2)
INSERT INTO funcionario(nome, id_funcionario_evento) values ('Rogério', 3)
INSERT INTO funcionario(nome, id_funcionario_evento) values ('Davi', 3)

INSERT INTO local(nome, capacidade, id_local_evento) values ('Salão de Festas Municipal', 250, 1)
INSERT INTO local(nome, capacidade, id_local_evento) values ('Restaurante Coffe, Campina Grande', 50, 2)
INSERT INTO local(nome, capacidade, id_local_evento) values ('Churrascaria do Pedrão', 100, 3)
