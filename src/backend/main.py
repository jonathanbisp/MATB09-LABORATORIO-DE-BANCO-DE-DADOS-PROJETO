from fastapi import FastAPI
from webapp.services.queriesManager import recreateDatabase
from webapp.services.queriesClient import criarCliente, obterClientePeloNome, obterClientePeloCPF,\
     obterClientePeloEmail, apagarClientePeloCPF #, atualizarClienteByCPF
from webapp.models.Cliente import Cliente, Nome, CPF, Email
from webapp.services.queriesVeiculo import criarVeiculo, obterVeiculoRevavam, obterVeiculoNumchassi, obterVeiculoModelo
from webapp.models.Veiculo import Veiculo, Revavam, Numchassi, Modelo
from webapp.services.queriesFuncionario import criarFuncionario, obterFuncionarioPeloNome, obterFuncionarioPeloCPF, obterFuncionarioPeloEmail
from webapp.models.Funcionario import Funcionario, Nome, CPF, Email
from webapp.services.queriesSeguro import criarSeguro,obterSeguroPeloNome,obterSeguroPeloCodigo,obterSeguroPeloValor
from webapp.models.Seguro import Seguro, Nome,Valor, Codigo
from webapp.services.queriesAluga import criarAluga,obterAlugaCPF,obterAlugaNumchassi,obterAlugaRevavam
from webapp.models.Aluga import Aluga,fk_cliente_cpf,fk_veiculo_revavam,fk_veiculo_numchassi


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



@app.post("/criarFuncionario")
def createFuncionario(funcionario: Funcionario):
    return criarFuncionario(funcionario.dict())

@app.get("/buscarFuncionario/nome")
def getFuncionarioByPartOfName(nome: Nome):
    return obterFuncionarioPeloNome(nome.dict())

@app.get("/buscarFuncionario/cpf")
def getFuncionarioByPartOfCPF(cpf: CPF):
    return obterFuncionarioPeloCPF(cpf.dict())

@app.get("/buscarFuncionario/email")
def getFuncionarioByPartOfEmail(email: Email):
    return obterFuncionarioPeloEmail(email.dict())

@app.delete("/apagarFuncionario/cpf")
def deleteFuncionarioByCPF(cpf: CPF):
    return apagarFuncionarioPeloCPF(cpf.dict())


@app.post("/criarSeguro")
def createSeguro(seguro: Seguro):
    return criarSeguro(seguro.dict())

@app.get("/buscarSeguro/nome")
def getSeguroByPartOfName(nome: Nome):
    return obterSeguroPeloNome(nome.dict())

@app.get("/buscarSeguro/codigo")
def getSeguroByPartOfCodigo(codigo: Codigo):
    return obterSeguroPeloCodigo(codigo.dict())

@app.get("/buscarSeguro/valor")
def getSeguroByPartOfValor(valor: Valor):
    return obterSeguroPeloValor(valor.dict())


@app.post("/criarAluga")
def createAluga(aluga: Aluga):
    return criarAluga(aluga.dict())

@app.get("/buscarAluga/revavam")
def getAlugaByRevavam(fk_veiculo_revavam: fk_veiculo_revavam):
    return obterAlugaRevavam(fk_veiculo_revavam.dict())

@app.get("/buscarveiculo/numchassi")
def getAlugaByNumChassi(fk_veiculo_numchassi: fk_veiculo_numchassi):
    return obterAlugaNumchassi(fk_veiculo_numchassi.dict())

@app.get("/buscarAluga/cpf")
def getAlugaByCPF(fk_cliente_cpf: fk_cliente_cpf):
    return obterVeiculoModelo(fk_cliente_cpf.dict())