import cherrypy
from database.Participantes import Participantes

class paginatabela():
    topo = open("view/layouts/cabecalho.html").read()
    @cherrypy.expose()
    def index(self):
        return self.montaTabela()

    def montaTabela(self):
        html = self.topo

        html += '''<table class="alinhar">
                    <br><br><br><br>
                     <tr> 
                        <th> CPF </th>
                        <th> Nome </th>
                        <th> Email </th>
                        <th> Curso </th> 
                        <th> Cidade </th>
                        <th colspan="2"> Opcao Desejada</th>       
                     </tr> '''
        # buscar os dados do banco de dados
        objParticipante = Participantes() # criamos um objeto do tipo Especie
        dados = objParticipante.obterParticipantes() # será criada uma lista com o resultado o SQL
        for linha in dados:
            html += ''' <tr>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td style="text-align: center;color: aqua;"">
                              <a  style="color: aqua;" href="alterarParticipante?cpf=%s" class="#">Alterar</a>
                           </td>
                           <td style="text-align:center;border: 1px solid red; color: red;">
                              <a  style="color: red;" href="excluirParticipantes?cpf=%s" class="#">Excluir</a>
                           </td>
                        </tr>
                        ''' % (linha['CPF'], linha['Nome'],linha['Email'],linha['Curso'],linha['Cidade'],linha['CPF'],linha['CPF'])
        html +=''' </table> <br> <br>'''

        return html
    
    
    @cherrypy.expose()
    def excluirParticipantes(self,cpf):
        objParticipantes = Participantes()
        objParticipantes.set_cpf(int(cpf))
        if objParticipantes.excluir() > 0: # informa se conseguiu excluir ou não
            raise cherrypy.HTTPRedirect('/register') # para atualizar a página após a exclusão (tipo reload)
        else:
            return '''
            <h2>Não foi possível excluir a espécie!!</h2>
            [<a href="/register">Voltar</a>]
            '''
    
    # @cherrypy.expose()
    # def alterarParticipante(self, cpf):
    #     objEspecie = Participantes()
    #     # buscar no banco a espécie que foi informada no parâmetro
    #     dadosEspecieSelec = objEspecie.obterParticipantes(cpf)
    #     # chamar o método para montar o formulário com os dados da espécie selecionada na tabela e carregar nos elementos <input> do formulário
    #     return self.montaTabela(
    #         dadosEspecieSelec[0]['CPF'],
    #         dadosEspecieSelec[0]['Nome'],
    #         dadosEspecieSelec[0]['Email'],
    #         dadosEspecieSelec[0]['Curso'],
    #         dadosEspecieSelec[0]['Cidade']
    #         ) @cherrypy.expose()

    @cherrypy.expose()
    def alterarParticipante(self, cpf):
        objParticipante = Participantes()
        participante = objParticipante.obterParticipantePorCPF(cpf)

        html = f'''
            {self.topo}
            <form method="post" action="salvarAlteracao" class="alinhar">
                <br><br><br><br><br><br><br><br>
                <input type="hidden" name="cpf" value="{participante['CPF']}">
                <label>Nome: </label><input type="text" name="nome" value="{participante['Nome']}" style="width: 300px;"><br>
                <br>
                <label>Email: </label><input type="text" name="email" value="{participante['Email']}" style="width: 300px;"><br>
                <br>
                <label>Curso: </label><input type="text" name="curso" value="{participante['Curso']}" style="width: 300px;"><br>
                <br>
                <label>Cidade: </label><input type="text" name="cidade" value="{participante['Cidade']}" style="width: 300px;"><br>
                <br>
                <input type="submit" value="Salvar Alterações" class="btnreg">
            </form>
        '''

        return html

    @cherrypy.expose()
    def salvarAlteracao(self, cpf, nome, email, curso, cidade):
        objParticipante = Participantes()
        objParticipante.atualizarParticipante(cpf, nome, email, curso, cidade)  # Implemente esta função em Participantes
        raise cherrypy.HTTPRedirect('/index')


        