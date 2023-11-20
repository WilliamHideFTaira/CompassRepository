--
-- Arquivo gerado com SQLiteStudio v3.4.4 em ter nov 7 17:46:29 2023
--
-- Codificação de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabela: Carros
CREATE TABLE IF NOT EXISTS Carros (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustiveis (idCombustivel)
);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (98, 25412, 'AKJHKN98JY76539', 'Fiat', 'Fiat Uno', 2000, 1);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (99, 20000, 'IKJHKN98JY76539', 'Fiat', 'Fiat Palio', 2010, 1);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (3, 121700, 'DKSHKNS8JS76S39', 'VW', 'Fusca 78', 1978, 1);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (10, 211800, 'LKIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996, 1);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (7, 212800, 'SSIUNS8JS76S39', 'Nissan', 'Versa', 2019, 1);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (6, 21800, 'SKIUNS8JS76S39', 'Nissan', 'Versa', 2019, 1);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (2, 10000, 'AKIUNS1JS76S39', 'Nissan', 'Versa', 2019, 2);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (4, 20000, 'AKIUNS1JS76S39', 'Nissan', 'Versa', 2019, 2);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (1, 1800, 'AAAKNS8JS76S39', 'Toyota', 'Corolla XEI', 2023, 3);
INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (5, 8500, 'MSLUNS1JS76S39', 'Toyota', 'Frontier', 2022, 4);

-- Tabela: Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    idVendedor INT,
    FOREIGN KEY (idVendedor) REFERENCES Vendedores (idVendedor)
);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (2, 'Cliente dois', 5);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (3, 'Cliente tres', 6);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (4, 'Cliente quatro', 7);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (6, 'Cliente seis', 8);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (10, 'Cliente dez', 16);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (20, 'Cliente vinte', 30);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (22, 'Cliente vinte e dois', 30);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (23, 'Cliente vinte e três', 30);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (5, 'Cliente cinco', 30);
INSERT INTO Clientes (idCliente, nomeCliente, idVendedor) VALUES (26, 'Cliente vinte e seis', 32);

-- Tabela: Combustiveis
CREATE TABLE IF NOT EXISTS Combustiveis (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);
INSERT INTO Combustiveis (idCombustivel, tipoCombustivel) VALUES (1, 'Gasolina');
INSERT INTO Combustiveis (idCombustivel, tipoCombustivel) VALUES (2, 'Etanol');
INSERT INTO Combustiveis (idCombustivel, tipoCombustivel) VALUES (3, 'Flex');
INSERT INTO Combustiveis (idCombustivel, tipoCombustivel) VALUES (4, 'Diesel');

-- Tabela: Locacoes
CREATE TABLE IF NOT EXISTS Locacoes (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria INT,
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Clientes (idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carros (idCarro)
);
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (1, 2, 98, '2015-01-10', '10:00', 2, 100, '2015-01-12', '10:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (2, 2, 98, '2015-02-10', '12:00', 2, 100, '2015-02-12', '12:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (3, 3, 99, '2015-02-13', '12:00', 2, 150, '2015-02-15', '12:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (4, 4, 99, '2015-02-15', '13:00', 5, 150, '2015-02-20', '13:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (5, 4, 99, '2015-03-02', '14:00', 5, 150, '2015-03-07', '14:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (6, 6, 3, '2016-03-02', '14:00', 10, 250, '2016-03-12', '14:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (7, 6, 3, '2016-08-02', '14:00', 10, 250, '2016-08-12', '14:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (8, 4, 3, '2017-01-02', '18:00', 10, 250, '2017-01-12', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (9, 4, 3, '2018-01-02', '18:00', 10, 280, '2018-01-12', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (10, 10, 10, '2018-03-02', '18:00', 10, 50, '2018-03-12', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (11, 20, 7, '2018-04-01', '11:00', 10, 50, '2018-04-11', '11:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (12, 20, 6, '2020-04-01', '11:00', 10, 150, '2020-05-21', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (13, 22, 2, '2022-05-01', '8:00', 10, 150, '2022-06-21', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (14, 22, 2, '2022-06-01', '8:00', 10, 150, '2022-07-21', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (15, 22, 2, '2022-07-01', '8:00', 10, 150, '2022-07-21', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (16, 22, 2, '2022-08-01', '8:00', 10, 150, '2022-08-01', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (17, 23, 4, '2022-09-01', '8:00', 10, 150, '2022-09-21', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (18, 23, 4, '2022-10-01', '8:00', 10, 150, '2022-10-21', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (19, 23, 4, '2022-11-01', '8:00', 10, 150, '2022-11-21', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (20, 5, 1, '2023-01-02', '18:00', 20, 880, '2023-01-12', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (21, 5, 1, '2023-01-15', '18:00', 20, 880, '2023-01-25', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (22, 26, 5, '2023-01-25', '18:00', 10, 600, '2023-01-30', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (23, 26, 5, '2023-01-31', '18:00', 10, 600, '2023-02-05', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (24, 26, 5, '2023-02-06', '18:00', 10, 600, '2023-02-11', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (25, 26, 5, '2023-02-12', '18:00', 10, 600, '2023-02-17', '18:00');
INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) VALUES (26, 26, 5, '2023-02-18', '18:00', 1, 600, '2023-02-19', '18:00');

-- Tabela: Vendedores
CREATE TABLE IF NOT EXISTS Vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (5, 'Vendedor cinco', 0, 'São Paulo');
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (6, 'Vendedora seis', 1, 'São Paulo');
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (7, 'Vendedora sete', 1, 'Rio de Janeiro');
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (8, 'Vendedora oito', 1, 'Minas Gerais');
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (16, 'Vendedor dezesseis', 0, 'Amazonas');
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (30, 'Vendedor trinta', 0, 'Rio Grande do Sul');
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (31, 'Vendedor trinta e um', 0, 'Ceará');
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (32, 'Vendedora trinta e dois', 1, 'Mato Grosso do Sul');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
