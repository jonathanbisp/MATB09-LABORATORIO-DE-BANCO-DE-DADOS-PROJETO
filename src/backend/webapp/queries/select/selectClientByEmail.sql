SELECT cpf, nomecompleto, pnome, unome, email FROM cliente WHERE UPPER(email) LIKE UPPER('%s')