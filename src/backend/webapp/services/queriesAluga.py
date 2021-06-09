import psycopg2
from psycopg2.errors import UniqueViolation
from webapp.services.utils import getSqlScript
from webapp.services.utils import notNull
from fastapi import HTTPException
from psycopg2.extras import RealDictCursor


def criarAluga(AlugaInfos):
    try:
        fk_cliente_cpf = notNull(AlugaInfos['fk_cliente_cpf'])
        fk_veiculo_Renavam = notNull(AlugaInfos['fk_veiculo_renavam'])
        fk_veiculo_numchassi = notNull(AlugaInfos['fk_veiculo_numchassi'])
        fk_funcionario_codigo = notNull(AlugaInfos['fk_funcionario_codigo'])
        fk_seguro_codigo = AlugaInfos['fk_seguro_codigo']
        datalocacao = notNull(AlugaInfos['datalocacao'])
        datadevolucao = notNull(AlugaInfos['datadevolucao'])
        status = notNull(AlugaInfos['status'])
        valor = notNull(AlugaInfos['valor'])
        parcelas = notNull(AlugaInfos['parcelas'])
        parcelaspagas= notNull(AlugaInfos['parcelaspagas'])
       
    except Exception as e:
        raise e
    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor()
    try:
        cur.execute(getSqlScript('insert/insertAluga'), (fk_cliente_cpf,
                    fk_veiculo_Renavam,
                    fk_veiculo_numchassi,
                    fk_funcionario_codigo,
                    fk_seguro_codigo,
                    datalocacao,
                    datadevolucao,
                    status,
                    valor,
                    parcelas,
                    parcelaspagas))
    except UniqueViolation:
            raise HTTPException(status_code=409, detail='Renavam ou numero de chassi já cadastrado')
    conn.commit()
    cur.close()
    conn.close()

    return {"detail": "Aluga cadastrado com sucesso"}


def obterAlugaRenavam(AlugaRenavam):
    try:
        Renavam = notNull(AlugaRenavam['fk_veiculo_Renavam'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectAlugaByRenavam').replace('%s', Renavam))
    
    data = cur.fetchall()
    
    cur.close()
    conn.close()

    return data


def obterAlugaNumchassi(AlugaNumchassi):
    try:
        numchassi = notNull(AlugaNumchassi['fk_veiculo_numchassi'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectAlugaByNumChassi').replace('%s', numchassi))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data


def obterAlugaCPF(Alugafk_cliente_cpf):
    try:
       fk_cliente_cpf= notNull(Alugafk_cliente_cpf['fk_cliente_cpf'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectAlugaByCPF').replace('%s', fk_cliente_cpf))
    print(getSqlScript('select/selectAlugaByCPF').replace('%s', fk_cliente_cpf))
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data