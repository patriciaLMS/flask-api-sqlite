Patrícia Lima Massolini RA: 1136999
Melhorias

Estrutura do Projeto: em vez de ter todo o código no mesmo arquivo, foi criada a separação de responsabilidades em diferentes módulos:

-db.py:  responsável pela interação com o banco de dados (criação de tabelas, inserção e recuperação de dados)
-auth.py: responsável por autenticação (login e verificação de token)

Autenticação e Validação:
Foi implementada uma função de login para validar o usuário
Foi adicionada a verificação do token JWT para proteger as rotas. O arquivo auth.py contém:

generate_token(username): gera um token JWT para o usuário.
login(): verifica as credenciais do usuário e gera um token.
verify_token(): verifica a validade do token fornecido nas requisições

As funções para a manipulação do banco de dados estavam no próprio app.py, agora a lógica de interação com o banco de dados foi movida para db.py o qual contém as funções:
connect_db(): cria a conexão com o banco de dados.
create_table(): cria a tabela no banco de dados.
insert_data(value): insere dados no banco de dados
fetch_data(): recupera dados no banco de dados

Rota de Login:
Foi adicionada uma rota /login para autenticação do usuário. Nessa rota, o usuário envia suas credenciais (usarname e  password) e, se forem válidas, um token JWT é retornado.
A lógica de busca dos dados foi movida para a função fetch_data() no arquivo db.py em vez de diretamente com o sqlite3.
