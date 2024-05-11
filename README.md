# Order Management API 

## Description

This is an Order Management API designed to help businesses manage their order efficiently.

<!-- TOC -->
* [Order Management API](#order-management-api-)
  * [Description](#description)
  * [Technologies](#technologies)
  * [Installation](#installation)
      * [1.Clone the Repository](#1clone-the-repository)
      * [2. Setup Virtual Environment with Poetry](#2-setup-virtual-environment-with-poetry)
      * [3. Install Dependencies](#3-install-dependencies)
      * [4. Setup Environment Variables](#4-setup-environment-variables)
  * [Project Structure](#project-structure)
  * [Usage](#usage)
    * [General Commands](#general-commands)
    * [Setup and Installation](#setup-and-installation)
    * [Linting](#linting)
    * [Code Complexity and Quality](#code-complexity-and-quality)
    * [Development and Testing](#development-and-testing)
    * [Production](#production)
<!-- TOC -->

## Technologies

* Python ~3.12
* FastAPI
* Poetry
* Make
* PostgresSQL
* SqlAlchemy
* Pydantic-settings
* Ruff
* Pytest

## Installation

#### 1.Clone the Repository

The first step is to clone the repository to your local environment.
This can be done using the `git clone` command followed by the repository URL.

```bash
git clone https://github.com/lucaschf/tech-challenge-phase-1.git
```

#### 2. Setup Virtual Environment with Poetry

Poetry is a tool for dependency management and packaging in Python.
Ensure that Poetry is installed on your system.
Then, create a virtual environment for the project using the command.

```bash
poetry env use 3.1*.*
poetry shell
```

see [python-poetry.org](https://python-poetry.org/docs/configuration/) for more information
about poetry.

#### 3. Install Dependencies

Use the `make` command to install all the project dependencies.
The `make install` command is used to install the dependencies listed in the `pyproject.toml` file.

```bash 
make install
```

#### 4. Setup Environment Variables

The project uses different `.env` files for different environments (test, dev, prod).
Create these files at the root of the project and fill them with the necessary variables.

| Env file  | Target environment |
|-----------|--------------------|
| .env      | development        |
| .env.dev  | development        |
| .env.test | test               |
| .env.prod | production         |

As you can see, there are four environment file names accepted.
You can use either `.env.dev` or `.env` to development environment.
But for prod and test environments only one `.env` file name is allowed

The necessary variables
to be placed in the `.env` files should be defined in the `Settings` class in
the `src.core.settings` module.
This class accepts default values, so in cases where default values are sufficient, you do not
need to define these variables in the `.env` files.

An example of the `.env` file is provided in the `.env.example` file.


## Project Structure

O projeto segue a **arquitetura hexagonal**, promovendo flexibilidade e testabilidade ao desacoplar 
a lógica de negócio de detalhes de implementação específicos.
Abaixo, detalhamos a estrutura de diretórios e o papel de cada componente:


- `src`: Diretório raiz do código-fonte do projeto.
  - `core`: Coração da aplicação, contendo a lógica de negócio e regras do domínio.
    - `application` Orquestra as ações do sistema.
      - `use_cases`: Casos de uso que definem as interações do usuário com o sistema e coordenam a execução das regras de negócio.
    - `domain`: Modelo do domínio do problema, independente de detalhes técnicos.
      - `base`:  Classes-base e utilitários que dão suporte às entidades do domínio.
      - `entities`: Representações dos objetos reais relevantes para o domínio, com seus atributos e comportamentos.
      - `exceptions`: Exceções personalizadas que capturam violações das regras de negócio, facilitando o tratamento de erros.
      - `repositories`: Interfaces que definem como as entidades do domínio são persistidas e recuperadas, permitindo a troca da implementação do armazenamento de dados sem afetar o domínio.
      - `value_objects`: Objetos imutáveis que representam conceitos do domínio, como dinheiro, 
        datas ou documentos.
    - `adapter`:Adaptadores que conectam o domínio a tecnologias externas.
      - `driven`: Adaptadores que o sistema usa, como bancos de dados, serviços de mensageiria ou APIs externas.
      - `driver`: Adaptadores que usam o sistema, como interfaces de usuário, APIs REST ou CLIs.
        - `api`: Implementação da API REST do sistema.
          - `controllers`: Controladores que recebem as requisições HTTP, interagem com os casos de uso e retornam as respostas. 
    - `config`: Configurações do projeto, como strings de conexão com o banco de dados, chaves de API e outras variáveis de ambiente.
- `tests`: Diretório que contém os testes automatizados do projeto.
  - (Subdiretórios e arquivos de teste organizados de forma espelhada à estrutura do código em 
    src, para facilitar a localização e manutenção dos testes.)

Essa estrutura hexagonal oferece diversas vantagens:

- `Testabilidade`: A lógica de negócio é isolada, facilitando a criação de testes unitários e de integração.
- `Flexibilidade`: A substituição de tecnologias é facilitada, pois as regras de negócio não dependem de detalhes de implementação.
- `Manutenibilidade`: A separação de responsabilidades torna o código mais organizado e fácil de entender, facilitando a manutenção e evolução do sistema.
- `Confiabilidade`: Os testes automatizados garantem que o sistema funcione conforme o esperado, mesmo após modificações no código.

## Usage

This project uses a Makefile to streamline various development tasks.
Below are the available make commands and their descriptions:

### General Commands

- **`make help`**: Displays help information by parsing this Makefile for targets and descriptions.

### Setup and Installation

- **`make install`**: Installs necessary dependencies and sets up hooks.
  This includes installing Python dependencies using Poetry,
  setting up Git pre-commit hooks, and installing a Gitlint hook for linting commits.

### Linting

- **`make lint-check`**: Lints source files without modifying them.
  It checks the code using ruff, 
- **`make lint-fix`**: Formats and fixes linting issues in source files using the same tools.
- **`make lint-check-tests`**: Lints test files without modifying them.
- **`make lint-fix-tests`**: Formats and fixes linting issues in test files.

### Code Complexity and Quality

- **`make cc`**: Calculates Cyclomatic Complexity using radon and ensures code complexity adheres to
  set standards using xenon.

### Development and Testing

- **`make dev`**: Runs the development server.
  It sets the environment to 'development' and starts
  the server with uvicorn, allowing auto-reload on changes.

- **`make test`**: Runs tests in the test environment.
  It uses pytest for testing and coverage for
  generating reports.

- **`make test-cov`**: Runs tests and generates a detailed coverage report.

### Production

- **`make run`**: Runs the production server.
