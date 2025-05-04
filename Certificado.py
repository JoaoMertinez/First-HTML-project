import cherrypy

class paginaCertificado():
    topo = open("view/layouts/cabecalho.html").read()
    rodape = open("view/layouts/rodape.html").read()

    @cherrypy.expose()
    def index(self):
        return self.MontaHtml()
    
    def MontaHtml(self):
        html = self.topo

        html += '''
        <div>
            <br><br><br><br>
            <h1><span>35ª Semana de Computação e Informática da FIPP/Unoeste (INFOESTE 2022)</span></h1>
            <br>
            <h3>Preencha o campo abaixo:</h3>
            <br>
            <label for="tnome">CPF:</label>
            <input type="text" name="tnome" size="80" maxlength="50" placeholder="CPF" autofocus="true" required="required"/>
            <input class="btnreg"  type="button" name="bmensagem" value="Verificar" onclick="alert('Verificado com sucesso!')"/>
            <br><br>
            <img src="/imagenstr/certificado.png" width="800px">

        </div>
        <br><br><br><br><br><br>
        '''

        #puxar o banco de dados aqui para fazer a consulta do cpf na tabela de registro

        html += self.rodape

        return html    

