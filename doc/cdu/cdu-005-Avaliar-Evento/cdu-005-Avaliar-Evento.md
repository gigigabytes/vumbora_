# CDU005. Avaliar Eventos

- **Ator principal**: Usuário Cadastrado
- **Atores secundários**: ...  
- **Resumo**: Será possível avaliar eventos da plataforma.
- **Pré-condição**: Estar logado no sistema, não ser produtora.
- **Pós-Condição**: Avaliação adicionada ao evento.

## Fluxo Principal
### Usuário avalia evento
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: |
|1-Usuário clica botão avaliação.
 || 2-O sistema mostra a págima referente a avaliações.
 || 3-Na página de avaliações, o sistema mostra a opção de avaliação com valor de 1 a 5 estrelas.||
 4-Usuário seleciona a quantidade de estrelas.
 || 5-O sistema salva a avaliação e mostra uma mensagem de sucesso.|


## Fluxos alternativos I
### Usuário opta por deixar comentário na avaliação, após avaliar com estrelas.
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: |
 6.1-Usuário escreve um comentário na área de texto exibida na página de avaliação.|| 
 6.2-Após escrever o comentário, aperta no botão "enviar comentário".
 || 6.3-O sistema salva o comentário, mostra uma mensagem de sucesso e adiciona o comentário junto a avaliação de estrela.|


## Fluxos Exceção I
### Usuário não preenche o campo de comentário
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: |
6.2.1-Usuário clica na botão enviar comentário sem ter escrito nada. 
||6.2.1-O sistema mostra uma mensagem informando a necessidade de preencher o campo e retorna para o passo 6.1 .|

<!-- Caso a ser elaborado -->
<!-- ## Fluxos Exceção II
### Usuário não seleciona quantidade de estrelas
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: |
4.1 - Usuário clica na botão enviar comentário sem ter dado uma quantidade de estrelas.
||4.2 - O sistema toma como padrão 5 estrelas e salva a avaliação.| -->