# 📌 Projeto Integrador

## Site de Cursos e Atividades Gratuitas por Bairro

------------------------------------------------------------------------

## 📖 Resumo

Este projeto consiste no desenvolvimento de uma API para um site que
disponibiliza cursos e atividades gratuitas organizadas por bairro e
data.

A plataforma permitirá que usuários visualizem cursos e atividades
disponíveis sem necessidade de login, podendo filtrar os resultados por
bairro e período.

O sistema contará com um único administrador responsável por cadastrar,
editar e excluir informações.

O objetivo do projeto é aplicar conceitos de:

-   Desenvolvimento de APIs REST\
-   Modelagem de banco de dados relacional\
-   Relacionamentos entre tabelas (1:N)\
-   Autenticação básica com token\
-   Organização em camadas no backend

------------------------------------------------------------------------

# 🎯 Funcionalidades

## 👤 Área Pública

-   Listar bairros\
-   Listar cursos\
-   Listar atividades\
-   Filtrar cursos por bairro\
-   Filtrar cursos por data\
-   Filtrar atividades por bairro\
-   Filtrar atividades por data

## 🔐 Área Administrativa

-   Login do administrador\
-   Cadastrar bairros\
-   Cadastrar cursos\
-   Cadastrar atividades\
-   Editar registros\
-   Excluir registros

------------------------------------------------------------------------

# ⚙️ Stack do Backend

## 🐍 Linguagem: Python

Python foi escolhido por possuir:

-   Sintaxe simples e legível\
-   Curva de aprendizado acessível\
-   Boa aceitação no mercado\
-   Excelente suporte para desenvolvimento de APIs

------------------------------------------------------------------------

## 🚀 Framework: FastAPI

O FastAPI será utilizado para criação da API REST.

Principais motivos:

-   Desenvolvimento rápido e organizado\
-   Validação automática de dados\
-   Documentação automática (Swagger)\
-   Boa performance\
-   Uso de tipagem para maior clareza do código

------------------------------------------------------------------------

## 🗄️ Banco de Dados: SQLite

Será utilizado SQLite como banco relacional.

Motivos da escolha:

-   Não requer instalação de servidor\
-   Armazena dados em arquivo único\
-   Simples de configurar\
-   Adequado para projetos acadêmicos

------------------------------------------------------------------------

## 🔗 ORM: SQLAlchemy

O SQLAlchemy será utilizado para:

-   Mapear classes Python para tabelas do banco\
-   Criar modelos organizados\
-   Gerenciar relacionamentos entre entidades\
-   Evitar escrita manual excessiva de SQL

------------------------------------------------------------------------

## 📄 Validação de Dados: Pydantic

O Pydantic será utilizado para:

-   Validar dados recebidos nas requisições\
-   Definir schemas de entrada e saída\
-   Garantir tipos corretos (datas, strings, inteiros)

------------------------------------------------------------------------

## 🔐 Autenticação: JWT

Será implementado um sistema simples de autenticação utilizando JSON Web
Token (JWT) para o administrador.

### Fluxo:

1.  Admin realiza login.\
2.  O sistema gera um token.\
3.  O token deve ser enviado nas requisições protegidas.\
4.  Apenas rotas de criação, edição e exclusão exigem autenticação.

Rotas de consulta (GET) permanecem públicas.

------------------------------------------------------------------------

## ▶️ Servidor de Desenvolvimento: Uvicorn

O Uvicorn será utilizado para executar a aplicação localmente durante o
desenvolvimento.

Permite recarregamento automático ao salvar alterações no código.

------------------------------------------------------------------------

# 🗂️ Estrutura Inicial do Projeto

``` bash
app/
│
├── main.py
├── database.py
│
├── models/
├── schemas/
├── routers/
└── services/
```

------------------------------------------------------------------------

# 🧠 Modelagem de Dados (Resumo)

O sistema contará com as seguintes entidades:

-   Bairro\
-   Curso\
-   Atividade\
-   Admin

### Relacionamentos principais:

-   Um bairro pode ter vários cursos (1:N)\
-   Um bairro pode ter várias atividades (1:N)\
-   Um curso pertence a um único bairro (N:1)\
-   Uma atividade pertence a um único bairro (N:1)

------------------------------------------------------------------------

# 📌 Justificativa Geral da Arquitetura

A stack escolhida é:

-   Moderna\
-   Leve\
-   Didática\
-   Adequada ao prazo de dois meses\
-   Suficiente para aplicação de conceitos acadêmicos

O projeto prioriza organização, clareza e boas práticas sem adicionar
complexidade desnecessária.
