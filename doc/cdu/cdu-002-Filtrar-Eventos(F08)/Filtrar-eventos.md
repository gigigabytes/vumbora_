
**Vumbora?** 

**Especificação de Caso de Uso**

**Filtragem de Eventos**

**Histórico da Revisão**

|**Data**|**Versão**|**Descrição**|**Autor**|
| :-: | :- | -: | :-: |
|08/10/2023|1\.0|< Primeiro plano >|< Rafael Silveira >|
|dd/mm/aaaa|1\.1|<breve descrição da revisão>|<autores da revisão>|

1. # **Resumo**

*O sistema precisa ser capaz de filtrar os eventos a partir de opções pré-estabelecidas nos critérios de valor, gênero e data. O sistema deve oferecer as seguintes opções pré determinadas dentro dos critérios, valor: Gratuito, até 10 reais, até 30 reais, até 50 reais e acima de 50. Data: Hoje, essa semana, esse mês, próximo mês. Gênero: Show, bairro, gastronomia, teatro, festas, exposições.* 

2. # **Atores**
**	Usuário do site, público geral e Agência.

3. # **Precondições**

*Sem precondições.*

4. # **Pós-condições**

`	`*Sem pós-condição.*

5. # **Fluxos de evento**

**5.1 Fluxo básico**

- *[IN] Usuário escolhe a opção de filtrar os eventos por gênero, valor ou data.*
- *[OUT] Sistema abre página de resultados com o tipo de evento escolhido e oferece a possibilidade de filtrar também com os dois outros critérios.*
- *[IN] Usuário escolhe adicionar ou não mais critérios na filtragem e confirma a opção caso decida adicionar.*
- *[OUT] Sistema retorna os resultados pertinentes.*
- *[IN] Usuário escolhe um evento.*
- *[OUT] Sistema abre a página de descrição do evento escolhido.*

# **5.2 Fluxo alternativo 1**

*4. [OUT] Sistema informa que não existem eventos condizentes com os critérios escolhidos e oferece a opção de voltar para a página anterior.*

*5. [IN] Usuário escolhe voltar para a página anterior e escolhe novos parâmetros.* 

*6.[OUT] Sistema retorna para o passo 4 do fluxo básico.* 



