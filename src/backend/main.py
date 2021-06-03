from fastapi import FastAPI
from webapp.services.queriesManager import recreateDatabase
from webapp.services.queriesClient import criarCliente, obterClientePeloNome, obterClientePeloCPF,\
     obterClientePeloEmail, apagarClientePeloCPF #, atualizarClienteByCPF
from webapp.models.Cliente import Cliente, Nome, CPF, Email
from webapp.services.queriesVeiculo import criarVeiculo, obterVeiculoRevavam, obterVeiculoNumchassi, obterVeiculoModelo
from webapp.models.Veiculo import Veiculo, Revavam, Numchassi, Modelo


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

@app.delete("/apagarCliente/cpf")
def deleteClientByCPF(cpf: CPF):
    return apagarClientePeloCPF(cpf.dict())

# permite atualizar tudo menos o proprio cpf
@app.patch('/atualizarCliente/cpf')
def updateClientByCPF(cliente: Cliente):
    return atualizarClienteByCPF(cliente.dict())


@app.post("/criarVeiculo")
def createVeiculo(veiculo: Veiculo):
    return criarVeiculo(veiculo.dict())

@app.get("/buscarVeiculo/revavam")
def getVeiculoByRevavam(revavam: Revavam):
    return obterVeiculoRevavam(revavam.dict())

@app.get("/buscarveiculo/numchassi")
def getVeiculoByNumChassi(numchassi: Numchassi):
    return obterVeiculoNumchassi(numchassi.dict())

@app.get("/buscarVeiculo/modelo")
def getVeiculoByModelo(modelo: Modelo):
    return obterVeiculoModelo(modelo.dict())