# GalinaceosApi

Este projeto é uma atividade da disciplina de Programação para Web II, no qual seu objetivo é praticar os conhecimentos adquiridos em Flask. As exigências deste projeto são:

- Implementar uma Api que contenha um endpoint chamado /galinaceos que aceite os filtros: SIST_CRIA, NIV_TERR, COD_TERR, NOM_TERR, CL_GAL;
- A aplicação deve persistir os dados no PostgreSQL (Docker).

## Criando um banco de dados com o docker

No terminal, execute o seguinte comando:

```bash
docker run --name galinaceos20261 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=123456 \
  -e POSTGRES_DB=galinaceos \
  -p 5435:5432 \
  -d postgres:18.4-alpine3.23
```

## Criando variáveis de ambiente

No arquivo [.env.example](.env.example) contém as variáveis de ambiente, no qual para que a conexão com o banco seja estabelecida, é necessário você criar um arquivo chamado ".env" na raíz do projeto e colar as informações do .env.example nele.

## Como executar o projeto

1. Abra o terminal e navegue até a pasta do projeto;
2. Digite o seguinte comando para criar um ambiente virtual:

    ```bash
    python3 -m venv .venv
    ```

3. Depois de criar o ambiente virtual, é preciso ativá-lo.
    - No Linux, execute o seguinte comando:

        ```bash
        source .venv/bin/activate
        ```
    - No cmd do Windows, execute o seguinte comando:

        ```bash
        .venv\Scripts\activate.bat
        ```
4. Com o ambiente virtual criado, é necessário instalar as dependências do projeto, para fazer isto, execute o seguinte comando:

    ```bash
    pip install -r requirements.txt
    ```

5. Para executar o projeto, execute o seguinte comando:

    ```bash
    flask run --debug
    ```

6. Quando terminar de executar o projeto, é necessário desativar o ambiente virtual, para desativá-lo, execute o seguinte comando:

    ```bash
    deactivate
    ```