-- Criação do banco
CREATE DATABASE gc;
USE gc;
-- Criação das tabelas

-- Tabela Condominio
CREATE TABLE Condominio (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    quant_torres INT,
    quant_andares INT,
    nome_condominio VARCHAR(255) NOT NULL,
    tipo VARCHAR(50),
    data_entrada DATE
);

-- Tabela Localizacao
CREATE TABLE Localizacao (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    condominio_id INT NOT NULL,
    uf VARCHAR(2),
    cidade VARCHAR(255),
    bairro VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    FOREIGN KEY (condominio_id) REFERENCES Condominio(ID)
);

-- Tabela Morador
CREATE TABLE Morador (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nome_responsavel VARCHAR(255) NOT NULL,
    cpf_responsavel VARCHAR(11) NOT NULL,
    data_entrada DATE
);

-- Tabela Morador_condominio
CREATE TABLE Morador_condominio (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    morador_id INT NOT NULL,
    condominio_id INT NOT NULL,
    apartamento VARCHAR(10),
    quant_moradores INT,
    FOREIGN KEY (morador_id) REFERENCES Morador(ID),
    FOREIGN KEY (condominio_id) REFERENCES Condominio(ID)
);