## Notícias API
Esta é uma API RESTful simples para gerenciar notícias.

## Endpoints
Listar Notícias
GET /news

Obter Notícia Específica
GET /news/{id}

Criar Nova Notícia
POST /news

Atualizar Notícia
PUT /news/{id}

Deletar Notícia
DELETE /news/{id}

## Exemplo de Requisição
Para criar uma nova notícia:

## Parâmetros Opcionais
data_criacao: Data de criação da notícia (formato YYYY). Este parâmetro é opcional e tem um valor padrão de 'N/A' se não for fornecido.
Códigos de Status
200 OK: Operação realizada com sucesso.
201 Created: Notícia criada com sucesso.
204 No Content: Notícia deletada com sucesso.
400 Bad Request: Requisito mal formulado ou campos obrigatórios ausentes.
404 Not Found: Notícia não encontrada.
405 Method Not Allowed: Método HTTP usado não é permitido para esse endpoint.
500 Internal Server Error: Erro interno do servidor.
