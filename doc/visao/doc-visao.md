**Documento de Visão**

**Histórico da Revisão**


|**Data**|**Versão**|**Descrição**|**Autor**|
| :-: | :-: | :-: | :-: |
|27/09/2023|1\.0|<Primeira versão da descrição> |<Giovanna, Leonardo, Matheus e Rafael> |
|08/10/2023|1\.1|<Unificação do tipo de usuário, ajustes nos requisitos, adição da agenda de eventos e ajustes gerais.>|<Rafael> |

1. **Projeto**: *VUMBORA?*
2. **Descrição do problema:**

|**O problema de** |Falta de uma plataforma que centralizasse os eventos da cidade.|
| :- | :- |
|**afeta**|Produtores de eventos e público geral que não visualizam com facilidade os eventos locais.|
|**cujo impacto é**|Empobrecimento da vida cultural da cidade.|
|**um boa solução seria**|Criar uma plataforma que irá facilitar o acesso a agenda cultural da cidade e oferecer a possibilidade de centralizar os eventos de produtores locais;|

3. **Descrição dos usuários:**

|**Nome**|**Descrição**|**Responsabilidade**|
| - | - | - |
|Usuário comum.|<p>**Usuário comum:**  Todas as pessoas interessadas na busca dos eventos natalenses e em divulgar os seus eventos. </p><p></p>|<p><p>**Usuário comum**: Busca os eventos, cadastra seus eventos e avalia eventos.</p><p></p>|

4. **Descrição do ambiente dos usuários:**

O ambiente para os usuários comuns, que são as pessoas que usarão a plataforma  para visualizar os eventos, seria a filtragem para a procura de eventos por localização, valor, lugar ou data, a visualização da descrição desses eventos e a possibilidade de acessar links pela plataforma para a possível compra do ingresso para o evento.

O ambiente para os produtores culturais seria fazer inserções de eventos adicionando as informações pertinentes relacionadas a eles como descrição, data, valor, onde comprar ingressos e localização. Essa ambientação, assim como todas as funções do sistema, é dependente da internet para o funcionamento.


5. **Principais necessidades dos usuários:**

`	`As pessoas que procuram eventos na cidade de Natal enfrentam a dificuldade de não ter uma plataforma específica que abarque a maior parte dos eventos disponíveis localmente, isso acontece porque as plataformas mais conhecidas estão focadas na venda de ingressos e por isso não mostram festividades que estão sob responsabilidade de outros sites. Nesse momento, os usuários precisam saber dos eventos por sua rede de conhecidos ou procurar em cada plataforma separadamente. Para resolver esse problema é preciso criar um espaço focado na divulgação de todos os eventos regionais sem discriminar por plataforma de venda, ajudando assim os usuários a encontrar os eventos que mais os interessem com facilidade.

Ademais, a divulgação dos eventos não é eficaz o suficiente para atingir uma parcela considerável da população.  Isso acontece porque a divulgação dos eventos ocorre de forma pulverizada em diferentes plataformas em acordo com qual delas está vendendo os ingressos. Dessa forma, um site faz a escolha de não mostrar eventos que não esteja trabalhando para não oferecer publicidade a outras plataformas. Assim, os espaços de divulgação se multiplicam e dificultam a vida de quem está interessado em saber as opções que tem. Dessa forma, no momento é preciso ir em várias plataformas e páginas específicas para descobrir quais eventos irão acontecer nos locais de interesse. Portanto, a principal solução para o usuário do sistema seria conseguir concentrar a visualização de eventos locais disponíveis.

6. **Alternativas concorrentes:**

O Sympla, Outgo, Gandaya e Ingresse seriam alternativas concorrentes que disponibilizam ações como as de: Filtrar eventos por localização, o Sympla faz a separação de eventos por temas de eventos, descrever detalhes dos eventos e também a opção de fazer com que os produtores de eventos possam adicionar seu evento na plataforma.

7. **Visão geral do produto:**

O projeto Vumbora?, trata-se de um um sistema onde possibilitará divulgações de eventos na cidade Natal/RN, em um nicho, a princípio, mais restrito. Nessas divulgações, estará incluso a descrição dos eventos como: a localização, data e hora, linkagem para compra de ingresso, caso precise, e todas outras descrições necessárias para a divulgação.
O sistema terá que filtrar os eventos por sua data, tema e valor para que a procura seja facilitada. Será criada uma agenda de eventos para facilitar a visualização dos eventos desejados em diferentes formas. 
Os usuários classificarão os eventos e as pessoas que os produziram para que exista um tipo de feedback para os outros usuários e as pessoas responsáveis pelos eventos. Dessa maneira, a plataforma irá se diferenciar em relação às outras pelo foco na divulgação dos eventos pertinentes para cada pessoa além de possibilitar uma historização dos pontos fortes e fracos de cada evento e pessoa que os produz. 

8. **Requisitos FUNCIONAIS**
 

|**Código**|**Nome**|**Descrição**|
| :- | :- | :- |
|*F01*|*Cadastro de usuários comuns*|*Realização de criação de perfil englobando alguns dados básicos dos usuários.*|
|*F02*|*Pesquisa dos eventos* |*Os usuários irão fazer pesquisas com intenção de encontrar eventos de acordo com sua preferência.*|
|*F03*|*Filtragem dos eventos*|*Os usuários fariam uma filtragem por tipo, local, valor ou data do evento.*|
|*F04*|*Inscrição dos eventos*|*Os produtores irão adicionar os eventos na plataforma com a descrição referente ao evento.*|
|*F05*|*Gerenciar a descrição dos eventos*|*Seria editar as informações dos eventos fazendo a atualização ou exclusão do evento, caso necessário.* |
|*F06*|*Gerenciar perfis*|*Realização de consulta e atualização de dados do perfil do usuário e/ou produtor.*|
|*F07*|*\*Classificar usuários que já produziram eventos*|*\*Os usuários poderão  avaliar os produtores de eventos para passar mais credibilidade.*|
|*F08*|*Filtragem dos usuários que já produziram eventos*|*Os usuários fariam uma busca dos produtores com a melhor avaliação no sistema.*|
|*F09*|*Favoritar um evento* |*O usuário poderá salvar um evento para ficar salvo para ele e/ou outros usuários que ele irá comparecer.*|
|*F10*|*Compartilhar evento* |*O usuário copiará o link do evento para compartilhamento.*|


9. **Requisitos NÃO-FUNCIONAIS**
   

|**Código**|**Nome**|**Descrição**|**Categoria**|**Classificação**<br>|
| :- | :- | :- | :-: | :-: |
|*RNF01*|*Design Responsivo*|*O sistema deve se adaptar a diferentes tamanhos de tela.*|*Usabilidade*|*Obrigatório*|
|*RNF02*|*Facilidade de uso*|*O sistema deve ser intuitivo e fácil de utilizar*|*Usabilidade*|*Obrigatório*|
|*RNF03*|*Troca de dados*|*O sistema deve se utilizar de um serviço de mapas como o google maps para informar o local dos eventos.*|*Interoperabilidade*|*Obrigatório*|



