CREATE TABLE IF NOT EXISTS sistema_criacao(
    id SERIAL PRIMARY KEY,
    sigla VARCHAR NOT NULL,
    descricao VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS nivel_territorial(
    id SERIAL PRIMARY KEY,
    sigla VARCHAR NOT NULL,
    descricao VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS codigo_territorial(
    id SERIAL PRIMARY KEY,
    codigo INT NOT NULL,
    descricao VARCHAR
);

CREATE TABLE IF NOT EXISTS nome_territorio(
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS classe_cabeca_galinaceos(
    id SERIAL PRIMARY KEY,
    codigo INT NOT NULL,
    descricao VARCHAR NOT NULL
);