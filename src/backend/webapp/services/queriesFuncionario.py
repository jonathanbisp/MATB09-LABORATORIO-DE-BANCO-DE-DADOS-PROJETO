import psycopg2
from psycopg2.errors import UniqueViolation
from webapp.services.utils import getSqlScript
from webapp.services.utils import validCPF, validEmail, validNasciment, notNull, validTelefoneBrasileiro
from fastapi import HTTPException
from psycopg2.extras import RealDictCursor


def criarFuncionario(funcionarioInfos):
    try:
        cpf = validCPF(funcionarioInfos['cpf'])
        codigo=funcionarioInfos['codigo']
        anonasc = validNasciment(funcionarioInfos['anonasc'])
        cargo=funcionarioInfos['cargo']
        nomecompleto = funcionarioInfos['nomecompleto']
        email = validEmail(funcionarioInfos['email'])
        senha = notNull(funcionarioInfos['senha'])
        fk_codigo_supervisor= funcionarioInfos['fk_codigo_supervisor']

        try:
            imglink = funcionarioInfos['imglink']
        except HTTPException as e:
            raise e
    except Exception as e:
        raise e
    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor()
    try:
        if len(fk_codigo_supervisor)!=0:
            cur.execute(getSqlScript('insert/insertFuncionario'), (cpf,codigo,nomecompleto,anonasc,cargo,email,senha,imglink,fk_codigo_supervisor))
        else:
            cur.execute(getSqlScript('insert/insertFuncionario'), (cpf,codigo,nomecompleto,anonasc,cargo,email,senha,imglink,None))
    except UniqueViolation:
            raise HTTPException(status_code=409, detail='Codigo ou CPF já cadastrado')
    conn.commit()
    cur.close()
    conn.close()

    return {"detail": "Funcionario cadastrado com sucesso"}


def obterFuncionarioPeloNome(funcionarioNome):
    try:
        nome = notNull(funcionarioNome['nome'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectFuncionarioByName').replace('%s', nome))
    
    data = cur.fetchall()
    
    cur.close()
    conn.close()

    return data


def obterFuncionarioPeloCPF(funcionarioCPF):
    try:
        cpf = notNull(funcionarioCPF['cpf'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectFuncionarioByCPF').replace('%s', cpf))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data


def obterFuncionarioPeloEmail(funcionarioEmail):
    try:
        email = notNull(funcionarioEmail['email'])
    except Exception as e:
        raise e

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('select/selectFuncionarioByEmail').replace('%s', email))
    
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data

def apagarFuncionarioPeloCPF(FuncionarioCPF):
    try:
        cpf = notNull(FuncionarioCPF['cpf'])
    except Exception as e:
        raise e
    
    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(getSqlScript('delete/deleteFuncionarioByCPF').replace('%s', cpf))
    
    conn.commit()
    cur.close()
    conn.close()
    return 'Apagado com sucesso'