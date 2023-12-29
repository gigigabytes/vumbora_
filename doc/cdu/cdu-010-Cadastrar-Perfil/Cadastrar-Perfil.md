# CDU008. Cadastrar Perfil

- **Ator principal**: Público geral
- **Atores secundários**: ...	 
- **Resumo**: O sistema deve mostrar a página com o formulário requisitando as seguintes informações: nome, email, tipo(Físico ou Jurídico), identidade(CPF para físico e CNPJ para jurídico) e foto(não precisa necessariamente ser fornecido), senha e confirmação da senha. 
- **Pré-condição**: Sem pré-condição
- **Pós-Condição**: Usuário deve está logado e salvo no sistema.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 0 - Usuário clica no botão de login enquanto não está logado no sistema. | 1 - Sistema exibe o formulário requisitando as seguintes informações: nome, email, tipo(Físico ou Jurídico), identidade(CPF para físico e CNPJ para jurídico) e foto(não precisa necessariamente ser fornecido), senha e confirmação da senha. | 
2 - Usuário preenche todos os campos obrigatórios e clica em registrar. | 3 - Sistema retorna para tela inicial e manda mensagem dizendo que operação foi bem sucedida. |

## Fluxo de exceção - Campo errado ou inexistente 
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2 - Usuário deixa de preencher um campo ou preenche de forma que não corresponde aos parâmetros estabelecidos necessários(sendo eles: os dois campos de senha não serem iguais; identidade ter um número que ainda já foi cadastrado) e clica em registrar. | 3 - Sistema retorna a mensagem que valor não é aceitável e diz qual foi o problema encontrado.|
4 - Fluxo retorna para o passo 2 do fluxo principal. | 
