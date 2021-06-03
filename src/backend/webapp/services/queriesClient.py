import psycopg2
from psycopg2.errors import UniqueViolation
from webapp.services.utils import getSqlScript
from webapp.services.utils import validCPF, validEmail, validNasciment, notNull, validTelefoneBrasileiro
from fastapi import HTTPException
from psycopg2.extras import RealDictCursor


def criarCliente(userInfos):
    try:
        cpf = validCPF(userInfos['cpf'])
        nomecompleto = userInfos['nomecompleto']
        anonasc = validNasciment(userInfos['anonasc'])
        telpessoal = validTelefoneBrasileiro(userInfos['telpessoal'])
        email = validEmail(userInfos['email'])
        senha = notNull(userInfos['senha'])

        try:
            telcomercial = validTelefoneBrasileiro(userInfos['telcomercial'])
            imglink = userInfos['imglink']
        except HTTPException as e:
            raise e
    except Exception as e:
        raise e
    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor()
    try:
        cur.execute(getSqlScript('insert/insertCliente'), (cpf, nomecompleto, pnome, unome, anonasc, telcomercial, telpessoal, email, senha, imglink))
    except UniqueViolation:
            raise HTTPException(status_code=409, detail='E-mail ou CPF já cadastrado')
    conn.commit()
    cur.close()
    conn.close()

    return {"detail": "Cliente cadastrado com sucesso"}


def obterClientePeloNome(clienteNome):
    try:
        nome = notNull(clienteNome['nome'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectClientByName').replace('%s', nome))
    
    data = cur.fetchall()
    
    cur.close()
    conn.close()

    return data


def obterClientePeloCPF(clientCPF):
    try:
        cpf = notNull(clientCPF['cpf'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectClientByCPF').replace('%s', cpf))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data


def obterClientePeloEmail(clientEmail):
    try:
        email = notNull(clientEmail['email'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectClientByEmail').replace('%s', email))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data


def apagarClientePeloCPF(clientCPF):
    try:
        cpf = notNull(clientCPF['cpf'])
    except Exception as e:
        raise e
    
    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('delete/deleteClientByCPF').replace('%s', cpf))
    
    conn.commit()
    cur.close()
    conn.close()
    return 'Apagado com sucesso'
