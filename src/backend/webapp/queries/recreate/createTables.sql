CREATE TABLE cliente(
    cpf character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL, 
    nomecompleto character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    anonasc date NOT NULL,
    telcomercial character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    telpessoal character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    email character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    senha character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    imglink character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
        CONSTRAINT cliente_pkey PRIMARY KEY (cpf),
        UNIQUE(email)
);
CREATE TABLE veiculo(
    renavam character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    numchassi character varying(17) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    modelo character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    anofabricacao date NOT NULL,
    imglink character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
        CONSTRAINT veiculo_pkey PRIMARY KEY (renavam, numchassi),
        UNIQUE(renavam),
        UNIQUE(numchassi)
);
CREATE TABLE funcionario(
    cpf character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    codigo serial NOT NULL,
    nomecompleto character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    anonasc date NOT NULL,
    cargo character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    email character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    senha character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    imglink character varying(255) COLLATE pg_catalog."pt-BR-x-icu",
    fk_codigo_supervisor integer,
    CONSTRAINT funcionario_pkey PRIMARY KEY (cpf, codigo),
    UNIQUE(codigo),
    CONSTRAINT fk_funcionario_2 FOREIGN KEY (fk_codigo_supervisor)
        REFERENCES funcionario (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
CREATE TABLE seguro(
    codigo serial NOT NULL,
    nome character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    descricao text COLLATE pg_catalog."pt-BR-x-icu",
    valor real NOT NULL,
    fk_veiculo_renavam character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    fk_veiculo_numchassi character varying(17) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    CONSTRAINT seguro_pkey PRIMARY KEY (codigo),
    CONSTRAINT fk_seguro_2 FOREIGN KEY (fk_veiculo_numchassi, fk_veiculo_renavam)
        REFERENCES veiculo (numchassi, renavam) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT
);
CREATE TABLE aluga(
    fk_cliente_cpf character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    fk_veiculo_renavam character varying(11) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    fk_veiculo_numchassi character varying(17) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    fk_funcionario_codigo integer NOT NULL,
    fk_seguro_codigo integer,
    datalocacao date NOT NULL,
    datadevolucao date NOT NULL,
    status character varying(255) COLLATE pg_catalog."pt-BR-x-icu" NOT NULL,
    valor real NOT NULL,
    parcelas integer NOT NULL,
    parcelaspagas integer NOT NULL,
    CONSTRAINT aluga_pkey PRIMARY KEY (fk_cliente_cpf, fk_veiculo_renavam, fk_veiculo_numchassi, fk_funcionario_codigo, datalocacao),
    CONSTRAINT fk_aluga_2 FOREIGN KEY (fk_cliente_cpf)
        REFERENCES cliente (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT,

    CONSTRAINT fk_aluga_3 FOREIGN KEY (fk_veiculo_numchassi, fk_veiculo_renavam)
        REFERENCES veiculo (numchassi, renavam) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT,

    CONSTRAINT fk_aluga_4 FOREIGN KEY (fk_funcionario_codigo)
        REFERENCES funcionario (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT,
    
    CONSTRAINT fk_aluga_5 FOREIGN KEY (fk_seguro_codigo)
        REFERENCES seguro (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE RESTRICT
);
