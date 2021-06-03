from fastapi import FastAPI
from webapp.services.queriesManager import recreateDatabase
from webapp.services.queriesClient import criarCliente, obterClientePeloNome, obterClientePeloCPF, obterClientePeloEmail
from webapp.models.Cliente import Cliente, Nome, CPF, Email
from webapp.services.queriesVeiculo import criarVeiculo, obterVeiculoRevavam, obterVeiculoNumchassi, obterVeiculoModelo
from webapp.models.Veiculo import Veiculo, Revavam, Numchassi, Modelo
from webapp.services.queriesFuncionario import criarFuncionario, obterFuncionarioPeloNome, obterFuncionarioPeloCPF, obterFuncionarioPeloEmail
from webapp.models.Funcionario import Funcionario, Nome, CPF, Email



app = FastAPI()

@app.get("/recreateDB")
def home():
    return recreateDatabase()


@app.post("/criarCliente")
def createUser(cliente: Cliente):
    return criarCliente(cliente.dict())

@app.get("/buscarCliente/nome")
def getClientByPartOfName(nome: Nome):
    return obterClientePeloNome(nome.dict())

@app.get("/buscarCliente/cpf")
def getClientByPartOfName(cpf: CPF):
    return obterClientePeloCPF(cpf.dict())

@app.get("/buscarCliente/email")
def getClientByPartOfName(email: Email):
    return obterClientePeloEmail(email.dict())



@app.post("/criarVeiculo")
def createVeiculo(veiculo: Veiculo):
    return criarVeiculo(veiculo.dict())

@app.get("/buscarVeiculo/revavam")
def getVeiculoByRevavam(revavam: Revavam):
    return obterVeiculoRevavam(revavam.dict())

@app.get("/buscarveiculo/numchassi")
def getVeiculoByNumChassi(numchassi: Numchassi):
    return obterVeiculoNumchassi(cpf.dict())

@app.get("/buscarVeiculo/modelo")
def getVeiculoByModelo(modelo: Modelo):
    return obterVeiculoModelo(modelo.dict())



@app.post("/criarFuncionario")
def createFuncionario(funcionario: Funcionario):
    return criarFuncionario(funcionario.dict())

@app.get("/buscarFuncionario/nome")
def getFuncionarioByPartOfName(nome: Nome):
    return obterFuncionarioPeloNome(nome.dict())

@app.get("/buscarFuncionario/cpf")
def getFuncionarioByPartOfName(cpf: CPF):
    return obterFuncionarioPeloCPF(cpf.dict())

@app.get("/buscarCliente/email")
def getClientByPartOfName(email: Email):
    return obterFuncionarioPeloEmail(email.dict())
