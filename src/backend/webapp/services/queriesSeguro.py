import psycopg2
from psycopg2.errors import UniqueViolation
from webapp.services.utils import getSqlScript
from webapp.services.utils import notNull
from fastapi import HTTPException
from psycopg2.extras import RealDictCursor


def criarSeguro(seguroInfos):
    try:
        valor=seguroInfos['valor']
        descricao=seguroInfos['descricao']
        nome = seguroInfos['nome']
        fk_veiculo_renavam=seguroInfos['fk_veiculo_renavam']
        fk_veiculo_numchassi= seguroInfos['fk_veiculo_numchassi']
    except Exception as e:
        raise e
    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor()
    try:
        cur.execute(getSqlScript('insert/insertSeguro'), (nome,descricao,valor,fk_veiculo_renavam,fk_veiculo_numchassi))
    except UniqueViolation:
        raise HTTPException(status_code=409, detail='Codigo já cadastrado')
    conn.commit()
    cur.close()
    conn.close()

    return {"detail": "Seguro cadastrado com sucesso"}


def obterSeguroPeloNome(seguroNome):
    try:
        nome = notNull(seguroNome['nome'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectSeguroByNome').replace('%s', nome))
    print(getSqlScript('select/selectSeguroByNome').replace('%s', nome))
    data = cur.fetchall()
    
    cur.close()
    conn.close()

    return data


def obterSeguroPeloCodigo(seguroCodigo):
    try:
        codigo = notNull(seguroCodigo['codigo'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectSeguroByCodigo').replace('%s', codigo))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data


def obterSeguroPeloValor(seguroValor):
    try:
        valor = notNull(seguroValor['valor'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectSeguroByValor').replace('%s', valor))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data