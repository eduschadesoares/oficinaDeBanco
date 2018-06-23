CREATE TABLE Cidade (
  CodIBGE VARCHAR(10) NOT NULL,
  Nome VARCHAR(100) NOT NULL,
  Idcidade INTEGER NOT NULL,
  PRIMARY KEY(Idcidade)
);

CREATE TABLE Cliente (
  Endereco VARCHAR(100) NOT NULL,
  Idcliente INTEGER NOT NULL,
  Ativo BIT NOT NULL,
  Idpj INTEGER NOT NULL,
  Idcidade INTEGER NOT NULL,
  PRIMARY KEY(Idcliente)
);

CREATE TABLE Entrega (
  Identrega INTEGER NOT NULL,
  Qtdeentregue NUMERIC(15, 2) NOT NULL,
  Dataentrega VARCHAR(10) NOT NULL,
  Iditempedido INTEGER NOT NULL,
  Idtransportadora INTEGER NOT NULL,
  PRIMARY KEY(Identrega)
);

CREATE TABLE Itempedido (
  Idproduto INTEGER NOT NULL,
  Idpedido INTEGER NOT NULL,
  Qtdevendida NUMERIC(15, 2) NOT NULL,
  Iditempedido INTEGER NOT NULL,
  Precounitario NUMERIC(15, 2) NOT NULL,
  PRIMARY KEY(Iditempedido)
);

CREATE TABLE Pagamento (
  Idpagamento INTEGER NOT NULL,
  Datapgto VARCHAR(10) NOT NULL,
  Valor NUMERIC(15, 2) NOT NULL,
  Tipopgto VARCHAR(1) NOT NULL,
  Idparcela INTEGER NOT NULL,
  PRIMARY KEY(Idpagamento)
);

CREATE TABLE Parcela (
  Idparcela INTEGER NOT NULL,
  Datavcto DATE NOT NULL,
  Valor NUMERIC(12, 2) NOT NULL,
  Tipopgto VARCHAR(1) NOT NULL,
  Idpedido INTEGER NOT NULL,
  PRIMARY KEY(Idparcela)
);

CREATE TABLE Pedido (
  Idpedido INTEGER NOT NULL,
  Nrpedido INTEGER NOT NULL,
  Idcliente INTEGER NOT NULL,
  PRIMARY KEY(Idpedido)
);

CREATE TABLE PessoaJuridica (
  Idpj INTEGER NOT NULL,
  Razaosocial VARCHAR(10) NOT NULL,
  PRIMARY KEY(Idpj)
);

CREATE TABLE Produto (
  Idproduto INTEGER NOT NULL,
  Nome VARCHAR(100) NOT NULL,
  PRIMARY KEY(Idproduto)
);
