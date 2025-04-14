CREATE TABLE paciente (
	id serial PRIMARY KEY,
  	nome varchar(70)
);

CREATE TABLE profissional (
	id serial PRIMARY KEY,
  	nome varchar(70),
  	especialidade varchar(50)
);

CREATE TABLE receita (
	id serial PRIMARY KEY,
  	receita text,
  	id_receita_paciente integer,
  	CONSTRAINT receita_paciente_fk FOREIGN KEY (id_receita_paciente) REFERENCES paciente(id) ON DELETE set null
);

CREATE TABLE consulta (
	id serial PRIMARY KEY,
  	data date,
  	id_consulta_profissional integer,
  	id_consulta_receita integer,
  	id_consulta_paciente integer,
  	CONSTRAINT consulta_profissional_fk FOREIGN KEY (id_consulta_profissional) REFERENCES profissional(id),
  	CONSTRAINT consulta_receita_fk FOREIGN KEY (id_consulta_receita) REFERENCES receita(id) ON DELETE set null,
  	CONSTRAINT consulta_paciente_fk FOREIGN KEY (id_consulta_paciente) REFERENCES paciente(id) ON DELETE set null
);

-- 3 adições para cada tabela
INSERT INTO paciente(nome) values ('Ramon');
INSERT INTO paciente(nome) values ('Jeferson');
INSERT INTO paciente(nome) values ('Kaik');

INSERT INTO profissional(nome, especialidade) values ('Renata', 'Ortopedista');
INSERT INTO profissional(nome, especialidade) values ('Anne', 'Dentista');
INSERT INTO profissional(nome, especialidade) values ('Arlindo', 'Médico geral');
INSERT INTO profissional(nome, especialidade) values ('Antônio', 'Enfermeiro');
INSERT INTO profissional(nome, especialidade) values ('Arthur', 'Enfermeiro');

INSERT INTO receita(receita, id_receita_paciente) values ('2 capsulas de dipirona. 2 capsulas de paracetamol', 1);
INSERT INTO receita(receita, id_receita_paciente) values ('3 copos de leite. Biscoitos a vontade.', 2);
INSERT INTO receita(receita, id_receita_paciente) values ('Melhorar alimentação. Fazer exercícios.', 3);

INSERT INTO consulta(data, id_consulta_profissional, id_consulta_receita, id_consulta_paciente) values ('2024-07-30', 1, 1, 1);
INSERT INTO consulta(data, id_consulta_profissional, id_consulta_receita, id_consulta_paciente) values ('2024-07-30', 2, 2, 2);
INSERT INTO consulta(data, id_consulta_profissional, id_consulta_receita, id_consulta_paciente) values ('2024-07-30', 3, 3, 3);
