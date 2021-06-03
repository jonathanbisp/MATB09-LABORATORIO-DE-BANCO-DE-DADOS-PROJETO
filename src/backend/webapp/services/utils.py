import re
from datetime import datetime
from fastapi import HTTPException

def getSqlScript(path):
    with open('./webapp/queries/'+ path + '.sql') as sql_file:
        return sql_file.read()


def validCPF(cpf):
    cpf = cleanCPF(cpf)
    if len(cpf) == 11:
        if cpf.isdigit():
            return cpf
        raise HTTPException(status_code=400, detail='CPF possui só possui números')
    raise HTTPException(status_code=400, detail='CPF possui 11 digitos')


def cleanCPF(cpf):
    return str(cpf).replace(".", "").replace("-", "")


def validEmail(email):
    regex = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if (re.match(regex, email)):
        return email
    print(re.match(regex, email))
    raise HTTPException(status_code=400, detail='E-mail não é válido')


def validNasciment(date):
    regex = '^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$'
    if (re.match(regex, date)):
        if datetime.strptime(date, '%Y-%m-%d') <= datetime(datetime.today().year -18, datetime.today().month, datetime.today().day):
            return date
        raise HTTPException(status_code=400, detail='Cliente não pode ser menor de idade.')
    raise HTTPException(status_code=400, detail='Formato incorreto, tente "YYYY-MM-DD"')

def notNull(content):
    if len(content) == 0:
        raise HTTPException(status_code=400, detail='Este campo não aceita o vazio')
    else:
        return content


def validTelefoneBrasileiro(telefone):  
    if telefone != None:
        regex = "([0-9]{3}|[0-9]{2})([0-9]{2})([0-9]{4,5})([0-9]{4})"

        resposta = re.search(regex, telefone)
        if resposta != None:
            return '+{}({}){}-{}'.format(resposta.group(1),  resposta.group(2), resposta.group(3), resposta.group(4))
        raise HTTPException(status_code=400, detail='Telefone inválido. Deve estar preenchido como a seguir para telefone móvel 05571982345389 e 0557182345389 para fixo')
    return None
