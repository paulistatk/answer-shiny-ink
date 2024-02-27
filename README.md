Este é um aplicativo de autenticação de chave de API que usa o Spring Boot, Spring Security e Servlet API. Ele permite que os usuários acessem recursos protegidos por API usando uma chave de API extraída do cabeçalho X-API-KEY.
Aqui está um resumo do que o projeto faz:
Configuração de Segurança:
O arquivo <security.xml> define as regras e restrições de segurança do aplicativo.
O acesso a todos os recursos é restrito, exigindo autenticação.
A autenticação é gerenciada por meio de uma chave de API extraída do cabeçalho HTTP X-API-KEY.
A geração de token e a validação são gerenciadas por AuthenticationService.
Filtro de autenticação:
Um AuthenticationFilter personalizado é usado para interceptar as solicitações de entrada e extrair a chave de API do cabeçalho X-API-KEY.
A chave de API é então usada para criar um ApiKeyAuthentication token, que é colocado no contexto de segurança.
Recurso protegido:
O controlador ResourceController contém um endpoint /home que retorna uma mensagem "Baeldung!" ao qual somente usuários autenticados podem acessar.
Para executar o projeto:
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
SPRING_PROFILES_ACTIVE=dev
Use code with caution.
Execute o comando mvn spring-boot:run na raiz do projeto para iniciar o aplicativo.
Use o comando curl para acessar o endpoint protegido:
curl --location --request GET 'http://localhost:8080/home' --header 'X-API-KEY:Baeldung' -v
Use code with caution.
Você deve receber a mensagem "Baeldung!" como resposta, indicando que o aplicativo está funcionando corretamente e a autenticação da chave de API está em vigor.
