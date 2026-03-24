# Tarefa 6
API de Apartamento e Moradores. A API Apartamento consulta Moradores e retorna os seguintes dados:
 - id
 - Numero do AP
 - Tamanho do AP
 - Nome do morador
 - Telefone do Morador
 
## Passo 1
Primeiro foi codifique a API Apartamento, que está no diretorio 'apartament'.

O código faz uma requisição simples para a API Morador e retorna os dados pegos da API junto com outros dados adicionados.

## Passo 2
Desenvolva a API Morador. A ideia é que receba requisições e responda com dados simulados.

## Passo 3
Crie arquivos 'DockerFile' para ambas as APIs, onde irão rodar separadamente. Cada arquivo cria o 'ambiente' isolado onde APIs irão funcionar.

## Passo 4
Criação do arquivo docker-compose, onde os containers são criados e uma rede interna, para a comunicação entre as APIs

## Passo 5
Rode o comando `sudo docker compose up --build` para iniciar os containers das APIs

## Passo 6
Realize testes. Os testes podem ser realizados por uma ferramenta da FastAPI. Primeiro entre na URL da API que se quer testar, por exemplo `http://localhost:8000/docs`
### Teste 1: Teste da API Morador 
![WhatsApp Image 2026-03-23 at 20 38 39](https://github.com/user-attachments/assets/fd8d0a8c-8957-45fb-a4b6-21a3189256c3)

A resposta foi o código HTTP 200, ou seja, foi um sucesso. Como também pode se observar, é retornado o corpo em json.

### Teste 2: Teste da API Apartamento
![WhatsApp Image 2026-03-23 at 20 38 39 (1)](https://github.com/user-attachments/assets/d5c56a24-d363-4217-8e24-933c523ec66c)

Como verificado no teste anterior, a API Morador está funcional. Agora, o serviço Apartamento se conecta a API Morador e retorna os dados requisitados a Morador e outros dados, também em JSON.

### Teste de Falha: 
Se API Morador demorar para responder (timeout padrão de 2 segundos) ou estiver fora do ar, então é retornado nenhum dado e a mensagem 'Serviço Indisponível'. 

### Possíveis problemas:
- API indisponível: A API pode não estar funcionando, não estar no ar;
- API demorando para responder: A API pode estar lidando com diversas requisições e demorar para responder, atingindo o timeout;
- Endpoint Incorreto: O Endpoint da API pode ser referenciado de forma errada, ou seja, a API nunca irá receber a requisição;
