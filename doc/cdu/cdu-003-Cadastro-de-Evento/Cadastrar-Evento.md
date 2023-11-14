# CDU003. Cadastrar Eventos

- **Ator principal**: Usuário cadastrado
- **Atores secundários**: ...	 
- **Resumo**: O usuário, caso queira, vai ter a possibilidade de cadastrar seu próprio evento, independente dele ser produtor ou não.
- **Pré-condição**: Usuário deve estar logado.
- **Pós-Condição**: O evento criado será publicado.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - O usuário escolhe a opção Cadastrar Evento | 2 -  Sistema abre uma página com formulário para o preenchimento das informações sobre o evento, o formulário deve requisitar nome, categoria do evento (Show, Teatro, Exposição, Gastronomia, Festa), imagens de divulgação, local, descrição de detalhes do evento (por exemplo: se o evento é pago e qual o valor da entrada), hora de início e de término do evento e informações sobre a produtora, como o nome e uma descrição sobre a mesma.  | 
| 3 - Usuário preenche as informações com os dados que são pedidos previamente no formulário e clica em publicar evento. | 4. Sistema verifica se todos os campos foram preenchidos e publica o evento com sucesso. |

## Fluxo Alternativo I - 3.1
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1. Usuário deixa algum campo em branco. | 2. Sistema verifica se todos os campos foram preenchidos e retorna o campo vazio que o usuário não preencher devidamente.|  
|3. Usuário preenche campos pendentes do formulário. | 4. Sistema finaliza caso de uso como no item 4 do Fluxo Principal.

