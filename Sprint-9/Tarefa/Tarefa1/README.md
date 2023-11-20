# Normalização do banco de dados
A normalização de um banco de dados envolve dividir a tabela em várias tabelas menores para eliminar redundâncias e garantir a integridade dos dados.

## Primeira Forma Normal (1NF)
Garantir que cada coluna contenha apenas valores atômicos. A tabela já atende a essa forma normal.

## Segunda Forma Normal (2NF)
A 2NF lida com a eliminação de dependências parciais e garante que cada coluna seja totalmente dependente da chave primária. Nessa tabela, a chave primária é a coluna "idLocacao". Para atingir a 2NF, é preciso separar as informações em tabelas distintas de modo que cada coluna esteja diretamente relacionada à chave primária:

Tabela 1: Locacoes
- idLocacao (PK)
- idCliente (FK para a tabela Clientes)
- idCarro (FK para a tabela Carros)
- idVendedor (FK para a tabela Vendedores)
- dataLocacao
- horaLocacao
- qtdDiaria
- vlrDiaria
- dataEntrega
- horaEntrega

Tabela 2: Clientes
- idCliente (PK)
- nomeCliente
- cidadeCliente
- estadoCliente
- paísCliente

Tabela 3: Carros
- idCarro (PK)
- kmCarro
- classiCarro
- marcaCarro
- modeloCarro
- anoCarro
- idCombustivel
- tipoCombustivel

Tabela 4: Vendedores
- idVendedor (PK)
- nomeVendedor
- sexoVendedor
- estadoVendedor

## Terceira Forma Normal (3NF)
Para alcançar a 3NF, é preciso garantir que não haja dependências transitivas entre as colunas. Nota-se isso na tabela Carros (idCombustível/tipoCombustível). O tratamento é feito criando uma nova tabela Combustíveis, mantendo idCombustivel na tabela Carros como chave estrangeira:

Tabela Combustiveis
- idCombustivel (PK)
- tipoCombustivel

## Resumo
Com a normalização, a tabela original foi dividida em cinco tabelas separadas para eliminar a duplicação de dados e garantir que todas as colunas sejam dependentes da chave primária correspondente. Cada tabela tem sua própria chave primária (PK) e relacionamentos podem ser estabelecidos entre as tabelas usando as chaves estrangeiras (FK) apropriadas, como **idCliente** e **idCarro** nas **Locacoes** referindo-se às respectivas tabelas de Clientes e Carros.
