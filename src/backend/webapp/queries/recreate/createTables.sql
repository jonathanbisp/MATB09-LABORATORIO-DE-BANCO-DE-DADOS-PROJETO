CREATE TABLE cliente(
    cpf character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL, 
    nomecompleto character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    pnome character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    unome character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    anonasc date,
    telcomercial character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    telpessoal character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    email character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    senha character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    imglink character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
        CONSTRAINT cliente_pkey PRIMARY KEY (cpf),
        UNIQUE(email)
);
CREATE TABLE veiculo(
    revavam character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    numchassi character varying(17) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    modelo character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    anofabricacao date,
    CONSTRAINT veiculo_pkey PRIMARY KEY (revavam, numchassi)
);
CREATE TABLE aluga(
    fk_cliente_cpf character varying(11) COLLATE pg_catalog."pt-BR-x-icu",
    fk_veiculo_revavam character varying(11) COLLATE pg_catalog."pt-BR-x-icu",
    fk_veiculo_numchassi character varying(17) COLLATE pg_catalog."pt-BR-x-icu",
    codigovendedor integer NOT NULL,
    codseguro integer,
    datalocacao integer,
    datadevolucao date,
    status character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    valor real,
    parcelas integer,
    parcelaspagas integer,
    CONSTRAINT aluga_pkey PRIMARY KEY (codigovendedor),
    CONSTRAINT fk_aluga_2 FOREIGN KEY (fk_cliente_cpf)
        REFERENCES cliente (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT,
    CONSTRAINT fk_aluga_3 FOREIGN KEY (fk_veiculo_numchassi, fk_veiculo_revavam)
        REFERENCES veiculo (numchassi, revavam) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT
);
CREATE TABLE funcionario(
    cpf character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    codigo integer NOT NULL,
    pnome character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    unome character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    anonasc date,
    cargo character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    nomecompleto character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    email character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    senha character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    imglink character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    fk_cpf_supervisor character varying(11) COLLATE pg_catalog."pt-BR-x-icu",
    fk_codigo_supervisor integer,
    fk_cliente_cpf character varying(11) COLLATE pg_catalog."pt-BR-x-icu",
    CONSTRAINT funcionario_pkey PRIMARY KEY (cpf, codigo),
    CONSTRAINT fk_funcionario_2 FOREIGN KEY (fk_codigo_supervisor, fk_cpf_supervisor)
        REFERENCES funcionario (codigo, cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_funcionario_3 FOREIGN KEY (fk_cliente_cpf)
        REFERENCES cliente (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT
);
CREATE TABLE seguro(
    codigo integer NOT NULL,
    nome character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    descricao text COLLATE pg_catalog."pt-BR-x-icu",
    valor real,
    fk_veiculo_revavam character varying(11) COLLATE pg_catalog."pt-BR-x-icu",
    fk_veiculo_numchassi character varying(17) COLLATE pg_catalog."pt-BR-x-icu",
    CONSTRAINT seguro_pkey PRIMARY KEY (codigo),
    CONSTRAINT fk_seguro_2 FOREIGN KEY (fk_veiculo_numchassi, fk_veiculo_revavam)
        REFERENCES veiculo (numchassi, revavam) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT
);