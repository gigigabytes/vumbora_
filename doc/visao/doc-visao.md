# Documento de Visão

## Histórico da Revisão

| Data      | Versão | Descrição                                         | Autor                             |
| --------- | ------ | ------------------------------------------------- | --------------------------------- |
| 27/09/2023| 1.0    | Primeira versão da descrição                      | Giovanna, Leonardo, Matheus e Rafael |
| 08/10/2023| 1.1    | Unificação do tipo de usuário, ajustes nos requisitos, adição da agenda de eventos e ajustes gerais. | Rafael |
| 13/11/2023| 1.2    | Ajustes gerais de compatibilidade                 | Giovanna, Leonardo, Matheus e Rafael |
| 26/02/2024| 1.3    | Ajustes básicos na descrição dos requisitos funcionais | Leonardo |

## 1. Projeto: VUMBORA?

## 2. Descrição do Problema:

| O problema de | Falta de uma plataforma que centralizasse os eventos da cidade. |
| -------------|--------------------------------------------------------------- |
| afeta        | Produtores de eventos e público geral que não visualizam com facilidade os eventos locais. |
| cujo impacto é | Empobrecimento da vida cultural da cidade. |
| uma boa solução seria | Criar uma plataforma que irá facilitar o acesso a agenda cultural da cidade e oferecer a possibilidade de centralizar os eventos de produtores locais. |

## 3. Descrição dos Usuários:

| Nome           | Descrição                                                                      | Responsabilidade                                                                                                                                               |
| -------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Usuário        | Pessoas físicas cadastradas na plataforma                                      | Cadastrar eventos, marcar presença, favoritar eventos e avaliar os eventos que participou.                                                                     |
| Público geral  | Todas as pessoas interessadas na busca dos eventos natalenses e em divulgar os seus eventos. | Procurar informações sobre eventos.                                                                                                                            |
| Produtora      | Pessoas jurídicas cadastradas na plataforma.                                    | Cadastrar eventos da produtora e responder comentários dos outros usuários em relação aos seus eventos.                                                       |

## 4. Descrição do Ambiente dos Usuários:

A plataforma deve funcionar todas as horas do dia e todos os dias, além disso, deve ser possível de acessar em qualquer lugar com acesso a internet e nos diferentes tipos de dispositivos.

## 5. Principais Necessidades dos Usuários:

As pessoas que procuram eventos na cidade de Natal enfrentam a dificuldade de não ter uma plataforma específica que abarque a maior parte dos eventos disponíveis localmente, isso acontece porque as plataformas mais conhecidas estão focadas na venda de ingressos e por isso não mostram festividades que estão sob responsabilidade de outros sites. Nesse momento, os usuários precisam saber dos eventos por sua rede de conhecidos ou procurar em cada plataforma separadamente. Para resolver esse problema é preciso criar um espaço focado na divulgação de todos os eventos regionais sem discriminar por plataforma de venda, ajudando assim os usuários a encontrar os eventos que mais os interessem com facilidade.

Ademais, a divulgação dos eventos não é eficaz o suficiente para atingir uma parcela considerável da população.  Isso acontece porque a divulgação dos eventos ocorre de forma pulverizada em diferentes plataformas em acordo com qual delas está vendendo os ingressos. Dessa forma, um site faz a escolha de não mostrar eventos que não esteja trabalhando para não oferecer publicidade a outras plataformas. Assim, os espaços de divulgação se multiplicam e dificultam a vida de quem está interessado em saber as opções que tem. Dessa forma, no momento é preciso ir em várias plataformas e páginas específicas para descobrir quais eventos irão acontecer nos locais de interesse. Portanto, a principal solução para o usuário do sistema seria conseguir concentrar a visualização de eventos locais disponíveis.


## 6. Alternativas Concorrentes:

O Sympla, Outgo, Gandaya e Ingresse seriam alternativas concorrentes que disponibilizam ações como as de: Filtrar eventos por localização, o Sympla faz a separação de eventos por temas de eventos, descrever detalhes dos eventos e também a opção de fazer com que usuários comuns possam cadastrar os seus eventos na plataforma, ensinando como fazer e oferecendo planos pagos que auxiliam na criação do evento e até mesmo pode se realizar o evento pela plataforma(no caso dele ser online). Entretanto, todas essas alternativas estão focadas na venda de ingressos, e assim, apenas estão inscritos na plataforma o evento que está sendo vendido por ela.  

## 7. Visão Geral do Produto:

O projeto Vumbora?, trata-se de um um sistema onde possibilitará divulgações de eventos na cidade Natal/RN, em um nicho, a princípio, mais restrito. Nessas divulgações, estará incluso a descrição dos eventos como: a localização, data e hora, linkagem para compra de ingresso, caso precise, e todas outras descrições necessárias para a divulgação. Além de possibilitar que o usuário cadastrado possa também criar seu evento para para divulgarção na plataforma.

O sistema filtrará os eventos por sua data, tema, valor e pelos eventos que irão acontecer na semana para que a procura seja facilitada. Será criada uma agenda de eventos para facilitar a visualização dos eventos desejados em diferentes formas. 

Os usuários classificarão os eventos e as pessoas que os produziram para que exista um tipo de feedback para os outros usuários e as pessoas responsáveis pelos eventos. Dessa maneira, a plataforma irá se diferenciar em relação às outras pelo foco na divulgação dos eventos pertinentes para cada pessoa além de possibilitar uma historização dos pontos fortes e fracos de cada evento e pessoa que os produz. 

## 8. Requisitos Funcionais:

| Código | Nome               | Descrição                                                                                   |
| ------ | ------------------ | ------------------------------------------------------------------------------------------- |
| F01    | Gerenciar eventos  | O usuário cria ou edita as informações dos eventos. Como também, atualiza ou exclui eventos, se necessário.   |
| F02    | Listar eventos da semana | Visualizar os eventos cadastrados que ocorrerão naquela semana.                            |
| F03    | Visualizar eventos cadastrados/favoritados | Ver os eventos que o usuário cadastrou ou favoritou.                                 |
| F04    | Pesquisar eventos  | Pesquisar eventos de acordo com a preferência do usuário.                                   |
| F05    | Detalhar evento    | Visualizar todos os detalhes públicos do evento.                                            |
| F06    | Favoritar evento   | Favoritar um evento para salvá-lo.                                                          |
| F07    | Avaliar evento     | O usuário pode avaliar de 0 a 5 estrelas os eventos.                                                                            |
| F08    | Comentar evento    | Comentar na página de um evento para deixar impressões ou tirar dúvidas.                     |
| F09    | Gerenciar perfis   | Cadastro, consulta, atualização de dados do perfil do usuário ou exclusão da conta.         |

## 9. Requisitos Não-Funcionais:

| Código | Nome                   | Descrição                                          | Categoria  | Classificação |
| ------ | ---------------------- | --------------------------------------------------| ---------- | ------------- |
| RNF01  | Design Responsivo      | Adaptar-se a diferentes tamanhos de tela.         | Usabilidade| Obrigatório   |
| RNF02  | Facilidade de uso      | Ser intuitivo e fácil de utilizar.                 | Usabilidade| Obrigatório   |

## Matriz de Rastreabilidade:

| Caso de Uso / Requisito | F01 | F02 | F03 | F04 | F05 | F06 | F07 | F08 | F09 |
|------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Detalhar Evento          |  X  |     |     |     |  X  |     |     |     |     |
| Listar Eventos(Semana)  |     |  X  |     |     |     |     |     |     |     |
| Pesquisar Eventos       |     |     |     |  X  |     |     |     |     |     |
| Cadastrar perfil        |     |     |  X  |     |     |     |     |     |  X  |
| Gerenciar Evento        |  X  |     |     |     |     |     |     |     |     |
| Visualizar Eventos Cadastrados/Favoritados |     |     |  X  |     |     |  X  |     |     |     |
| Comentar Evento         |     |     |     |     |     |     |  X  |     |     |
| Manter Perfil           |     |     |     |     |     |     |     |     |  X  |
| Favoritar Evento        |     |     |     |     |     |  X  |     |     |     |
| Avaliar Evento          |     |     |     |     |     |     |  X  |     |     |
