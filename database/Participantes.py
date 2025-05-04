from database.banco import Banco

class Participantes(): # está é o nome da classe de Espécies
    '''
        Documentação da classe
        - aqui nó vamos descrever os campos (propriedades) e funções (métodos) para definirmos de acordo com a teoria de Programação Orientada a Objetos
    '''
    # Construtor
    def __init__(self):
        # propriedades privadas
        self.__CPF = ''
        self.__Nome = ''
        self.__Email = ''
        self.__Curso =  ''
        self.__Cidade = ''
        self.__banco = Banco() # aqui será criado o objeto que representa o acesso ao Banco de Dados, nós iremos utilizar ela para gravar, excluir, alterar e buscar os dados já gravados no banco
        # propriedades públicas

    # definir os métodos para a nossa classe para colocar os valores nas propriedades
    def set_cpf(self, pCPF): # setar o valor é autoincremento
        if pCPF != 0: # validação dos valores para não serem negativos ou zerados, e serem corretamente associados à propriedade
            self.__CPF = pCPF

    def set_nome(self,pNome):
        if len(pNome) > 0:
            self.__Nome = pNome

    def set_email(self,pEmail):
        self.__Email = pEmail

    def set_curso(self,pCurso):
        self.__Curso = pCurso

    def set_cidade(self,pCidade):
        self.__Cidade = pCidade

    # métodos para obter os valores das propriedades
    def get_cpf(self):
        return self.__CPF

    def get_nome(self):
        return self.__Nome

    def get_email(self):
        return self.__Email
    
    def get_curso(self):
        return self.__Curso
    
    def get_cidade(self):
        return self.__Cidade

    # devolver todas as espécies cadastradas no banco de dados na tabela Especies
    def obterParticipantes(self):
        sql = '''
              SELECT CPF, Nome, Email, Curso, Cidade
              FROM Registro
              ORDER by CPF
              '''
        return self.__banco.executarSelect(sql)

    def gravar(self): # vai pegar os dados do objeto e gravar na tabela do banco
        sql = ''' INSERT INTO Registro (CPF, Nome, Email, Curso, Cidade)
                 values ("#cpf", "#nome", "#email", "#curso", "#cidade")
              '''
        sql = sql.replace('#cpf',self.__CPF)
        sql = sql.replace('#nome', self.__Nome)
        sql = sql.replace('#email',self.__Email)
        sql = sql.replace('#curso', self.__Curso)
        sql = sql.replace('#cidade',self.__Cidade)
        return self.__banco.executarInsertUpdateDelete(sql)

    # devolver uma espécia só cdastrada no banco de dados na tabela Especies
    def obterParticipante(self, pCPF=0):
        if pCPF != 0:
            self.__CPF = pCPF
        sql = ''' SELECT CPF, Nome, Email, Curso, Cidade
                  FROM Registro
                  where CPF = #cpf         '''
        sql = sql.replace('#cpf', str(self.__CPF))
        return self.__banco.executarSelect(sql)

    def excluir(self):
        sql = 'delete from Registro where CPF = #cpf'
        sql = sql.replace('#cpf', str(self.__CPF))
        return self.__banco.executarInsertUpdateDelete(sql)
    
    def obterParticipantePorCPF(self, cpf):
        sql = f"SELECT * FROM Registro WHERE CPF = '{cpf}'"
        resultado = self.__banco.executarSelect(sql)
        if resultado:
            return resultado[0]  # Retorna o primeiro registro encontrado
        else:
            return None

    def atualizarParticipante(self, cpf, nome, email, curso, cidade):
        sql = f'''UPDATE Registro
                  SET Nome = '{nome}', Email = '{email}', Curso = '{curso}', Cidade = '{cidade}'
                  WHERE CPF = '{cpf}'
               '''
        return self.__banco.executarInsertUpdateDelete(sql)
