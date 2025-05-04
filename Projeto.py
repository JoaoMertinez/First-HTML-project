import cherrypy
import os
from registro import paginaRegister
from Certificado import paginaCertificado
from tabelas import paginatabela


local_dir = os.path.dirname(__file__)

class principal():
    topo = open("view/layouts/cabecalho.html").read()
    paginaIni = open("view/infoeste.html").read()
    rodapePrincipal = open("view/layouts/rodapePrincipal.html").read()
    @cherrypy.expose()
    def index(self):
        html = self.topo
        
        html += '''
        <div class="fundo">
            <h1>35ª Infoeste</h1>
        </div>

        <div>
            <br>
            <h1 id="Sobre"><span>Sobre</span></h1> <br>
            <p class="paragrafo"> <span style="font-size: 30px;">A</span> Faculdade de Informática de Presidente Prudente
                (FIPP), da Universidade do Oeste Paulista (UNOESTE), realiza anualmente, a Semana de Computação e Informática da
                FIPP/Unoeste - INFOESTE.
                O evento, que é aberto a toda a comunidade regional e de outros centros, procura congregar estudantes de
                graduação e pós-graduação, professores, pesquisadores, profissionais e demais interessados em informática,
                objetivando a difusão da computação e informática e do seu bom uso, trazendo para o debate aberto temas
                importantes que indicam as tendências tecnológicas e do mercado atual, além da discussão de práticas pedagógicas
                no ensino superior, buscando atingir com mais ênfase os alunos dos cursos da FIPP/Unoeste.
                A INFOESTE 2023, que em sua 35ª edição, espera um público aproximado de 600 participantes, é promovida e
                organizada pela FIPP com apoio institucional da Sociedade Brasileira de Computação (SBC), UNOESTE e Associação
                das Empresas de Software do Oeste Paulista (POLOIN), e a colaboração de Docentes, Discentes, Funcionários,
                Empresa Júnior de Informática da Unoeste (UNINFO JR), Incubadora Tecnológica de Presidente Prudente (INTEPP),
                Diretório Acadêmico e Atlética da FIPP, Empresas Privadas/Públicas, IES Públicas/Privadas e Profissionais. <br>
                A INFOESTE 2023 contará com os seguintes eventos integrados: <br></p>
        </div>
        <br>
        <br>

        <div class="lista paragrafo">
            <li>35º Ciclo de Cursos e Palestras (Experience)</li>
            <li>17ª Maratona de Programação;</li>
            <li>09º FIPPETEC - Ciclo de Cursos para as ETECs;</li>
            <li>Certificação</li>
            <a href="/view/HistoriaInfoeste.html" class="container">
                <button>Historia Infoeste</button>
            </a>
            <img class="info" src="/imagenstr/Infoeste.Principal.jpeg" alt="Tentar novamente" width="500">
        </div>


        <br><br><br><br>
        <h1 id="eventos"><span>Eventos</span></h1>

        <div class="flex">
            <div class="eventos">

                <div class="polaroid">
                    <img src="/imagenstr/Maratona-Principal.jpg" alt="Tabela" style="width:100%">

                    <div class="container">
                        <a href="/view/Maratona.html">Maratona De Programação</a>
                    </div>
                </div>

                <div class="polaroid">
                    <img src="/imagenstr/Palestra.infoeste31.jpg" alt="Tabela" style="width:100%">

                    <div class="container">
                        <a href="/view/Palestras.html">35ª Ciclos De Palestras</a>
                    </div>
                </div>

                <div class="polaroid">
                    <img src="/imagenstr/Cursos.jpg" alt="Tabela" style="width:100%">

                    <div class="container">
                        <a href="/view/Cursos.html">Cursos Da 35ª Infoeste</a>
                    </div>
                </div>

                <div class="polaroid">
                    <img src="/imagenstr/Etec.jpg" alt="Tabela" style="width:100%">

                    <div class="container">
                        <a href="/view/FippEtec.html">9º FIPPETEC - Cursos</a>
                    </div>
                </div>


            </div>
        </div>
        <br>

        <p class="paragrafo">O evento, que é aberto a toda a comunidade regional e de outros centros, procura congregar
            estudantes de graduação e pós-graduação, professores, pesquisadores, profissionais e demais interessados em
            informática, objetivando a difusão da computação e informática e do seu bom uso, trazendo para o debate aberto temas
            importantes que indicam as tendências tecnológicas e do mercado atual, além da discussão de práticas pedagógicas no
            ensino superior, buscando atingir com mais ênfase os alunos dos cursos de Bacharelado em Ciência da Computação,
            Bacharelado em Sistemas de Informação, Analise desenvolvimento de sistemas da FIPP/Unoeste.</p>

        <a href="/view/edicoesAnter1.html" class="container">
            <button class="classBtn">Edições Anteriores</button>
        </a>
        <br><br><br><br><br>
        <div class="flex">
            <img src="/imagenstr/maps.fipp.png" alt="Loc.FIPP" height="100%" width="100%">
        </div>
        '''

        html += self.rodapePrincipal
        return html
    

server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 82
}
cherrypy.config.update(server_config)

#Para que o cherrypy possa encontrar os arquivos dentro do diretorio da aplicação
local_config={
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":local_dir},
}

root = principal()
root.register = paginaRegister()
root.certificado = paginaCertificado()
root.tabela = paginatabela()

cherrypy.quickstart(root,config=local_config)