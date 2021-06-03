import psycopg2
from psycopg2.errors import UniqueViolation
from webapp.services.utils import getSqlScript
from webapp.services.utils import validCPF, validEmail, validNasciment, notNull, validTelefoneBrasileiro
from fastapi import HTTPException
from psycopg2.extras import RealDictCursor


def criarVeiculo(veiculosInfos):
    try:
        revavam = notNull(veiculosInfos['revavam'])
        numchassi = notNull(veiculosInfos['numchassi'])
        modelo=veiculosInfos["modelo"]
        anofabricacao = veiculosInfos['anofabricacao']

        try:
            imglink = veiculosInfos['imglink']
        except HTTPException as e:
            raise e
    except Exception as e:
        raise e
    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor()
    try:
        cur.execute(getSqlScript('insert/insertVeiculo'), (revavam,numchassi,modelo,anofabricacao,imglink))
    except UniqueViolation:
            raise HTTPException(status_code=409, detail='Revavam ou numero de chassi já cadastrado')
    conn.commit()
    cur.close()
    conn.close()

    return {"detail": "Veiculo cadastrado com sucesso"}


def obterVeiculoRevavam(veiculoRevavam):
    try:
        revavam = notNull(veiculoRevavam['revavam'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectVeiculoByRevavam').replace('%s', revavam))
    
    data = cur.fetchall()
    
    cur.close()
    conn.close()

    return data


def obterVeiculoNumchassi(veiculoNumchassi):
    try:
        numchassi = notNull(veiculoNumchassi['numchassi'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectVeiculoByNumChassi').replace('%s', numchassi))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data


def obterVeiculoModelo(veiculoModelo):
    try:
        modelo = notNull(veiculoModelo['modelo'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectVeiculoByModelo').replace('%s', modelo))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data