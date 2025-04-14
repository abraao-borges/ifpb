-- 1 delete para cada tabela com where.
DELETE FROM paciente WHERE nome = 'Jeferson';
DELETE FROM profissional WHERE especialidade = 'Enfermeiro';
DELETE FROM receita WHERE id_receita_paciente = 3;
DELETE FROM consulta WHERE id_consulta_paciente = 2;

-- 1 update para cada tabela com where.
UPDATE paciente SET nome = 'Gela bacteria' WHERE nome = 'Kaik';
UPDATE profissional SET especialidade = 'Cirurgião' WHERE nome = 'Anne';
UPDATE receita SET receita = '1 copo de leite. Nem tantos biscoitos.' WHERE receita = '3 copos de leite. Biscoitos a vontade.';
UPDATE consulta SET data = '2024-08-06' WHERE id_consulta_paciente = 1;

-- 5 consultas.
SELECT * FROM consulta WHERE data = '2024-07-30';
SELECT * FROM paciente WHERE nome = 'Kaik'; -- deletado.
SELECT * FROM paciente WHERE id = 1;
SELECT * FROM profissional WHERE especialidade = 'Ortopedista';
SELECT * FROM receita WHERE id_receita_paciente = 1;
