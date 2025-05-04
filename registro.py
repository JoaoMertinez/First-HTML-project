import cherrypy
from database.Participantes import Participantes

class paginaRegister():
    topo = open("view/layouts/cabecalho.html").read()
    rodape = open("view/layouts/rodape.html").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()


    def montaFormulario(self, pCPF='', pNome='', pEmail='', pCurso='', pCidade=''):
        html = self.topo

        html += '''
        <br><br><br><br>
        <div>
            <h1 class="texto">REGISTRO</h1>
            <br>
        <form name="FormRegistro" action="gravarRegistro" method="post">
            <label for="tecpf">CPF:</label>
            <input type="number" name="tcpf" size="40" maxlength="30" placeholder="Digite seu CPF" autofocus="true" required="required" value="%s">
            <br><br/>
            <label for="tnome">Nome:</label>
            <input type="text" name="tnome" size="40" maxlength="30" placeholder="Digite seu nome" autofocus="true" required="required" value="%s">
            <br/><br/>
            <label for="temai">Email:</label>
            <input type="email" name="temai" size="40" maxlength="30" placeholder="Digite seu email" autofocus="true" required="required" value="%s">
            <br><br/>

            <ul style="text-align: left; ">
                <li>1- Criatividade e Geração de Ideias (MC01)</li>
                <li>2- Node.JS com Testes Unitários e Prisma (MC02)</li>
                <li>3- Introdução à Maratona de Programação (MC03)</li>
                <li>4- Empreendedorismo Tecnológico (MC04)</li>
                <li>5- O Essencial de GIT e GitHub (MC05)</li>
                <li>6- Marketing Digital (MC06)</li>
                <li>7- Intensivo ReactJS e Typescript (MC07)</li>
                <li>8- Scrum: Metodologia Ágil (MC10)</li>
                <li>9- Introdução ao Agile Thinking (MC11)</li>
                <li>10- Workshop sobre Testes de Capacidade com JMETER, K6 e GRAFANA (MC12)</li>
                <li>11- Workshop Introdução à Qualidade de Software, Automação, Alguns Frameworks, Cases e Aplicações (MC13)</li>
                <li>12- Introdução ao UX Design (MC14)</li>
                <li>13- Power BI (MC15)</li>
                <li>14- Introdução à Segurança da Informação com Linux (MC16)</li>
                <li>15- Práticas de Eletrônica Digital (MC17)</li>
                <li>16- Introdução a APIs REST com Node.js e Ferramentas de Testes Automatizados (MC18)</li>
                <li>17- Introdução ao GitHub (MC19)</li>
                <li>18- Blender 3D (ET01)</li>
                <li>19- Introdução ao Unity 3D (ET03)</li>
                <li>20- Produção de Conteúdo para o Instagram (ET07)</li>
                <li>21- Desenvolvimento Web para Iniciantes e Utilização de Frameworks CSS (ET09)</li>
                <li>22- 16ª Festa Linux para Principiantes</li>
                <li>23- 16ª Maratona de Programação da Faculdade de Informática de Presidente Prudente</li>
            </ul>
            <br/><br/>

            <label for="curso">Cursos:</label>
            <input type="curso" name="tcurso" size="40" maxlength="30" placeholder="Digite o curso desejado" autofocus="true" required="required" value="%s">
            <br/><br/>
            <label for="scid">Cidade:</label>
            <input type="ecid" name="tcid" size="40" maxlength="30" placeholder="Digite sua cidade" autofocus="true" required="required", value="%s">
            <br/>
            <input type="submit" id="btnGravar" name="btnGravar" value="Gravar" class="btnreg"/>
            <input class="btnreg"  type="reset" name="blimpar" value="Limpar"/>
        </form>
        </div>
        <br> <br> <br> <br> <br> <br><br> <br> <br> <br> <br> <br>
        ''' %(pCPF, pNome, pEmail, pCurso, pCidade)
        #puxar a função do banco de dados aqui
        html += self.rodape
        return html
    
    @cherrypy.expose()
    def gravarRegistro(self, tcpf, tnome, temai, tcid, tcurso, btnGravar):
        if len(tcpf) > 0:
            objParticipantes = Participantes()
            objParticipantes.set_cpf(tcpf)
            objParticipantes.set_nome(tnome)
            objParticipantes.set_email(temai)
            objParticipantes.set_cidade(tcid)
            objParticipantes.set_curso(tcurso)

            retorno = objParticipantes.gravar()
            
            if retorno > 0:
                return '''
                        <script>
                           alert("%s foi Cadastrada(o) com sucesso!!")
                           window.location.href = "/"
                        </script>
                       ''' % (tnome)