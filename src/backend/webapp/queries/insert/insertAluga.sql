INSERT INTO aluga (fk_cliente_cpf,
                    fk_veiculo_renavam,
                    fk_veiculo_numchassi,
                    fk_funcionario_codigo,
                    fk_seguro_codigo,
                    datalocacao,
                    datadevolucao,
                    status,
                    valor,
                    parcelas,
                    parcelaspagas) 
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)