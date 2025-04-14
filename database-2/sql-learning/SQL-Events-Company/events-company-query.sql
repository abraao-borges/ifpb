DELETE FROM cliente WHERE id_cliente_evento = 3;
DELETE FROM convidado WHERE id_convidado_evento = 3;
DELETE FROM servico WHERE id_servico_evento = 3;
DELETE FROM funcionario WHERE id_funcionario_evento = 3;
DELETE FROM local WHERE id_local_evento = 3;
DELETE FROM evento WHERE tipo = 'Chá de Revelação';

UPDATE evento SET tipo = 'Aniversário Particular' WHERE tipo = 'Aniversário Infantil';
UPDATE cliente SET nome = 'Souza de Amaral' WHERE nome = 'Amaral de Souza';
UPDATE convidado SET nome = 'Convidado do evento 1' WHERE id_convidado_evento = 1;
UPDATE servico SET tipo = 'Homem aranha acrobático' WHERE id_servico_evento = 1;
UPDATE funcionario SET nome = 'Nayara' WHERE nome = 'Pamela';
UPDATE local SET capacidade = 200 WHERE id = 2;

SELECT * FROM evento WHERE inicio = '2004-12-29 19:00:00';
SELECT * FROM cliente WHERE id_cliente_evento = 2;
SELECT * FROM convidado WHERE id_convidado_evento = 2;
SELECT * FROM funcionario WHERE nome = 'Pamela';
SELECT * FROM local WHERE capacidade > 200;
