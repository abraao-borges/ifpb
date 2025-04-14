-- Criar a tabela time
CREATE TABLE time(
	id serial PRIMARY KEY,
	nome varchar(50)
);

-- Criar a tabela jogador
CREATE TABLE jogador(
	id serial PRIMARY KEY,
	nome varchar(70),
	posicao varchar(15),
	id_time integer,
	CONSTRAINT jogador_time_fk FOREIGN KEY (id_time) REFERENCES time(id) ON DELETE set null
);

-- Criar a tabela tecnico
CREATE TABLE tecnico(
 	id serial PRIMARY KEY,
  	nome varchar(70),
  	id_time integer,
  	CONSTRAINT tecnico_time_fk FOREIGN KEY (id_time) REFERENCES time(id) ON DELETE set null
);

-- Criar a tabela estadio
CREATE TABLE estadio (
	id serial PRIMARY KEY,
  	nome varchar(50)
);

-- Criar a tabela partida
CREATE TABLE partida (
	id serial PRIMARY KEY,
	inicio varchar(8),
	sumula varchar(1000),
  	id_estadio integer,
  	id_tecnico_time_um integer,
  	id_tecnico_time_dois integer,
  	id_time_um integer,
  	id_time_dois integer,
	CONSTRAINT partida_estadio_fk FOREIGN KEY (id_estadio) REFERENCES estadio(id),
	CONSTRAINT partida_tecnico_time_um_fk FOREIGN KEY (id_tecnico_time_um) REFERENCES tecnico(id),
	CONSTRAINT partida_tecnico_time_dois_fk FOREIGN KEY (id_tecnico_time_dois) REFERENCES tecnico(id),
	CONSTRAINT partida_time_um_fk FOREIGN KEY (id_time_um) REFERENCES time(id),
	CONSTRAINT partida_time_dois_fk FOREIGN KEY (id_time_dois) REFERENCES time(id)
);

CREATE TABLE participacao (
	id serial PRIMARY KEY,
    gol integer,
    defesa integer,
    inicio varchar(8),
    id_participacao_jogador integer,
    id_participacao_partida integer,
    CONSTRAINT participacao_jogador_fk FOREIGN KEY (id_participacao_jogador) REFERENCES jogador(id),
    CONSTRAINT participacao_partida_fk FOREIGN KEY (id_participacao_partida) REFERENCES partida(id)    
);

CREATE TABLE arbitro (
	id serial PRIMARY KEY,
  	papel varchar(50),
  	id_arbitro_partida integer,
  	CONSTRAINT arbitro_partida_fk FOREIGN KEY (id_arbitro_partida) REFERENCES partida(id)
);

-- Inserir times
INSERT INTO time(nome) values ('Vasco');
INSERT INTO time(nome) values ('Flamengo');

-- Inserir jogaores
INSERT INTO jogador(nome, posicao, id_time) values ('Roberto Dinamite', 'Atacante', 1);
INSERT INTO jogador(nome, posicao, id_time) values ('João Carlos', 'Lateral-direito', 2);

-- Inserir tecnicos
INSERT INTO tecnico(nome, id_time) values ('Dorival', 1);
INSERT INTO tecnico(nome, id_time) values ('Pedroca', 2);

-- Inserir estadios
INSERT INTO estadio(nome) values ('Maracanã');

-- Inserir partidas
INSERT INTO partida(inicio, sumula, id_estadio, id_tecnico_time_um, id_tecnico_time_dois, id_time_um, id_time_dois) values ('12:00:00', 'Jogão da porra, terminou 3x0 pro time da casa. Roberto Dinamite carregou essa partida nas costas!', 1, 1, 2, 1, 2);

-- Inserir participação
INSERT INTO participacao(gol, defesa, inicio, id_participacao_jogador, id_participacao_partida) values (3, 0, '12:30:00', 1, 1);

-- Inserir arbitro
INSERT INTO arbitro(papel, id_arbitro_partida) values ('Cartão amarelo para o camisa 9.', 1);
