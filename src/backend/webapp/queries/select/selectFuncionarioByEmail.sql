SELECT cpf, nomecompleto, pnome, unome, email FROM funcionario WHERE UPPER(email) LIKE UPPER('%s')