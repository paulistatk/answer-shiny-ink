Este projeto implementa autenticação de chave de API com segredo, onde o segredo é uma string "Baeldung" que é passada no cabeçalho da solicitação "X-API-KEY". Se o segredo estiver correto, o usuário é autenticado e tem acesso ao endpoint "/home".

O projeto Spring Boot tem as seguintes características principais:

A classe SecurityConfig é responsável pela configuração da segurança da aplicação. Nele é criado um filtro de autenticação personalizado chamado AuthenticationFilter, que é adicionado à cadeia de filtros de segurança antes do UsernamePasswordAuthenticationFilter.

O filtro AuthenticationFilter tenta autenticar o usuário verificando se o segredo da chave da API está correto. Se estiver, o filtro define a autenticação no contexto de segurança e permite que a solicitação prossiga. Se não estiver, o filtro retorna um erro 401 Não autorizado.

A classe ApiKeyAuthentication é uma implementação personalizada do AbstractAuthenticationToken que é usada para representar a autenticação da chave de API.

O serviço AuthenticationService é responsável por obter a autenticação do usuário da solicitação HTTP. Ele verifica se o segredo da chave da API está correto e retorna uma instância de ApiKeyAuthentication se estiver.

A classe ResourceController contém o endpoint "/home" que é acessível somente por usuários autenticados.

Para usar o projeto, você precisa:

Criar um arquivo application.properties na raiz do projeto com o seguinte conteúdo:

spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration,org.springframework.boot.autoconfigure.security.servlet.UserDetailsServiceAutoConfiguration

Executar o projeto usando o comando mvn spring-boot:run.

Fazer uma solicitação GET para o endpoint "/home" passando o segredo da chave da API no cabeçalho "X-API-KEY". Por exemplo:

curl --location --request GET 'http://localhost:8080/home' --header 'X-API-KEY:Baeldung'

Se o segredo estiver correto, a solicitação será bem-sucedida e retornará a mensagem "Baeldung !". Se o segredo estiver incorreto, a solicitação retornará um erro 401 Não autorizado.
