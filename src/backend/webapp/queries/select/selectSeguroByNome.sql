SELECT codigo,nome,descricao,valor FROM seguro WHERE UPPER(nome) LIKE UPPER('%%s%')