## Sprint 2

A Sprint 2 tem foco em dois conteúdos que se complementam: [SQL](#sql), que é uma linguagem de consulta estruturada usada para armazenar e processar as informações em banco de dados, e [Big Data](#big-data), que é a área de conhecimento de analisar, tratar e obter informações úteis a partir de conjuntos de dados muito grandes

### SQL

SQL (Structured Query Language) é uma linguagem de consulta usada em banco de dados **relacional**, fazendo seleções em tabelas de acordo com parâmetros estabelecidos na consulta.

#### Criando tabelas no banco de dados

* O primeiro comando a se considerar é a construção de tabelas dentro de um banco de dados:

 ```
    CREATE TABLE nome_da_tabela(
        nome_da_coluna1 tipodacoluna1
        nome_da_coluna2 tipodacoluna2
)
```
**OBS**: tipo da coluna se refere ao tipo do valor que será inserido na coluna (ex: int, varchar etc)
* Para inserir valores dentro da tabela:

```
    INSERT INTO nome_da_tabela
    (nome_da_coluna1, nome_da_coluna2)

    values
    ('nome1', 'valor1'),
    ('nome2', 'valor2'),
    ('nome3', 'valor3')
```
* Podemos usar fazer correções de dados inseridos:

```
    UPDATE nome_da_tabela
    SET nome_da_coluna = 'novoValor'
    WHERE nome_da_coluna = 'valorAntigo'
```

* Para apagar uma linha de dados da tabela:
```
    DELETE FROM nome_da_tabela
    WHERE nome_da_coluna1 = 'valor1'
    OR nome_da_coluna2 = 'valor2'
```

* Para inserir uma coluna em uma tabela:
```
    ALTER nome_da_tabela
    ADD nova_coluna tipodacoluna
```

* Para alterar o tipo de uma coluna:
```
    ALTER TABLE nome_da_tabela
    ALTER COLUMN nome_da_coluna TYPE novo_tipo
```

* Para alterar o NOME de uma coluna:
```
    ALTER TABLE nome_da_tabela
    RENAME COLUMN nome_da_coluna TO novo_nome
```

* Para deletar uma coluna de uma tabela:
```
    ALTER TABLE nome_da_tabela
    DROP COLUMN nome_da_coluna
```

* Para deletar uma tabela do banco de dados:
```
    DROP TABLE nome_da_tabela
```

* Podemos criar também uma tabela a partir de outra tabela, usando `SELECT` com `INTO` (para entender SELECT, clique [aqui](#comandos-básicos)):
```
    SELECT
        nome_da_coluna_tb
        into nome_da_nova_tabela
    FROM tabela_tb
```

#### Comandos básicos

* Comando SELECT - seleciona coluna de uma tabela

    `SELECT coluna from tabela`

    `SELECT coluna1, coluna2 FROM tabela`

**OBS**: Use * apos SELECT para receber todas as colunas

    `SELECT * FROM tabela`

* Selecionar coluna de uma tabela **sem repetições**

    `SELECT DISTINCT coluna FROM tabela`

* Comando WHERE - filtro de pesquisa

    `SELECT coluna FROM tabela WHERE nome = 'NOME'`

    `SELECT coluna, nome FROM tabela WHERE nome = 'NOME' OR cpf = '99999999999'`

    `SELECT coluna, nome, birth_date WHERE nome = 'NOME' OR cpf = '99999999999' AND birth_date < '1991-12-28'`

* Comando ORDER BY - ordem crescente de pesquisa (desc para ordem decrescente)

    `SELECT coluna FROM tabela WHERE nome = 'NOME' ORDER BY coluna`

* Comando LIMIT - limita número de linhas da pesquisa

    `SELECT coluna_1, coluna_2 FROM tabela WHERE nome = 'NOME' ORDER BY coluna_1 limit 20`

#### Operações no SQL

É possível realizar operações matemáticas, comparativas e lógicas com SQL:
* Operadores aritméticos: + (soma), - (subtração), * (multiplicação), / (divisão), ^ (expoente), % (resto de divisão), || (**CONCATENA STRINGS**)
* Operadores de comparação: =, >, <, >=, <=, <> (geram retorno TRUE ou FALSE, usado com frequência com WHERE)
* Operadores lógicos: AND, OR, NOT, BETWEEN, IN, LIKE, ILIKE, IS NULL

#### Funções de agregação

* Para realizar operações aritméticas nos registros de uma coluna:
    * `COUNT(parâmetro)` - conta linhas de uma tabela de acordo com parâmetro(s);
    * `SUM(parâmetro)` - soma linhas de uma tabela de acordo com parâmetro(s);
    * `MIN(parâmetro)` - valor mínimo das linhas de uma tabela de acordo com parâmetro(s);
    * `MAX(parâmetro)` - valor mínimo das linhas de uma tabela de acordo com parâmetro(s);
    * `AVG(parâmetro)` - valor médio das linhas de uma tabela de acordo com parâmetro(s).
* `GROUP BY` - agrupa registros semelhantes de uma coluna (usado comumente com funções de agregação)
    ```
    SELECT
        COLUNA1, count(*) as CONTADOR
    FROM
        TABELA
    GROUP BY
        COLUNA1
    ORDER BY
        CONTADOR
    ```
* `HAVING` - filtra linhas da seleção por uma coluna agrupada
    ```
    SELECT 
        COLUNA1, 
        count(*)
    FROM TABELA
    GROUP BY COLUNA1
    HAVING count(*) > 100
    ```
#### JOIN

`JOIN` é a função para juntar tabelas, combinando colunas. A sintaxe é:
```
SELECT
    t1.coluna_1,
    t1.coluna_2,
    t2.coluna_1,
    t2.coluna_2
FROM
    schema.tabela_1 AS t1
ALGUM JOIN schema.tabela_2 AS t2
    ON condição_de_join
```

* **`INNER JOIN`**: Retorna apenas os registros que têm correspondência nas duas tabelas. Ou seja, ele combina registros com base nas colunas que têm valores iguais em ambas as tabelas;

* **`LEFT JOIN`**: Retorna todos os registros da tabela à esquerda (a primeira mencionada) e os registros correspondentes da tabela à direita (a segunda mencionada). Se não houver correspondência na tabela à direita, o resultado ainda terá todas as linhas da tabela à esquerda, mas com valores NULL nas colunas da tabela à direita.

* **`RIGHT JOIN`**: É semelhante ao LEFT JOIN, mas agora retorna todos os registros da tabela à direita e os registros correspondentes da tabela à esquerda. Se não houver correspondência na tabela à esquerda, o resultado ainda terá todas as linhas da tabela à direita, mas com valores NULL nas colunas da tabela à esquerda.

#### UNION

O comando **`UNION`** combina resultados de duas ou mais consultas em uma única saída. A sintaxe é:

```
SELECT coluna_1, coluna_2
FROM schema_1.tabela_1

UNION / UNION ALL

SELECT coluna_3, coluna_4 
FROM schema_2.tabela_2
```

A diferença do **UNION** para o **UNION ALL** é a duplicidade. O UNION ALL não remove registros duplicados. Ele combina todos os resultados das consultas individuais, enquanto o UNION mostra apenas um resultado se houver duplicatas.

#### Subquerys

Subquerys são subconsultas realizadas junto com a consulta, podendo ser realizadas:
* no **WHERE**:
```
    SELECT *
    FROM 
        TABELA
    WHERE 
        COLUNA = (
            SELECT
                min(COLUNA)
            FROM
                TABELA)
```
* no **FROM**:
```
    SELECT
        TABELANOVA.COLUNA1 AS NOME,
        TABELANOVA.COLUNA2 AS IDADE
    FROM (
        SELECT 
            COLUNA1,
            COLUNA2,
            COLUNA3
        FROM
            TABELA2
        WHERE
            COLUNA1 = 'PARAMETRO'
    ) AS TABELANOVA
```
* no **SELECT**:
```
    SELECT
    	coluna1,
    	(
	    	SELECT 
                count(*)
	        FROM 
                tabela2 AS tab2
    		WHERE 
                tab2.coluna2 <= tab1.coluna2
			    and tab2.coluna3 = tab1.coluna3
	    ) AS tab3
    FROM tabela1 AS tab1
    LEFT join tabela4 AS tab4
    	on tabela1.coluna3 = tab4.coluna3
    ORDER BY tab4.coluna1, tab1.coluna2
```
* com **WITH**:
```
    WITH tab1 AS (
    SELECT
	    coluna1,
	    coluna2 / 12 as par
    FROM tabela2
    )
```

#### Tratamento de dados

Consultas podem geram erros ou saídas inesperadas. Diante disso, existem uma série de formas de tratar os dados resultantes para melhor compreensão:

* Operador de **CONVERSÃO**- ::
```
    SELECT nome_coluna::date
    FROM nome_tabela
```
* Agrupamento de dados **CASE WHEN**
```
    SELECT
        valor,
        CASE
            WHEN valor < 10 then 'pequeno'
            WHEN valor > 10 and valor < 20 then 'médio'
            WHEN valor > 20 then 'grande'
            else 'muito grande'
            end as grandeza
    FROM tabela
```
* Dados nulo **COALESCE**
```
    SELECT
        *,
        CASE
            WHEN valor is not null then valor
            ELSE '0'
            END AS valor_novo
    FROM TABELA1
```
```
    SELECT
	    *,
	    COALESCE(coluna1, 
            (SELECT 
                avg(coluna1) 
                FROM tabela)
        ) AS novovalor
    FROM tabela
```

* **Tratamento de dados tipo texto**:
    * LOWER() - transforma todo o texto em letras minúsculas;
    ```
        SELECT lower('São Paulo') => 'são paulo'
    ```
    * UPPER() - transforma todo o texto em letras maiúsculas;
    ```
        SELECT upper('São Paulo') => 'SÃO PAULO'
    ```
    * TRIM() - remove espaços das extremidades de um texto;
    ```
        SELECT trim('SÃO PAULO     ') => 'SÃO PAULO'
    ```
    * REPLACE() - substitui uma string por outra.
    ```
        SELECT replace('SAO PAULO', 'SAO', 'SÃO') => 'SÃO PAULO'
    ```
* **Tratamento de dados tipo data**:
    * **INTERVAL** - utilizado para somar datas na unidade desejada. Caso a unidade não seja informada, o SQL irá entender que a soma foi feita em dias.
    ```
        SELECT (dtatual + INTERVAL '10 weeks')::date
        SELECT (dtatual + INTERVAL '10 months')::date
        SELECT dtatual + INTERVAL '10 hours'
    ```
    * **DATE_TRUNC** - utilizado para truncar uma data no início do período.
    ```
        SELECT
	        DATE_TRUNC('month', dtvisita)::date as dtvisitaMes, 
            count(*)
        FROM tabela1
    ```
    * **EXTRACT** - utilizado para extrair unidades de uma data/timestamp
    ```
        SELECT
	        EXTRACT('dow' from dtvisita) as weekD,
	        count(*)
        FROM tabela
        GROUP BY weekD
        ORDER BY weekD
    ```
    * Diferença entre datas: O cálculo da diferença entre datas com o operador de subtração **(-)** retorna valores em dias. 
    ```
        SELECT (dtatual - '2018-06-01') / 30
    ```
**Criação de funções**
* Servem para criar comandos personalizados de scripts usados recorrentemente.
    * Para criar uma função:
    ```
        CREATE FUNCTION nome_da_funcao (parâmetros)
        RETURNS tipo_de_retorno 
        LANGUAGE sql 
        AS
        $$
            --Corpo da função--
            --Instruções SQL aqui--
            --RETURN valor_de_retorno--
        $$
    ```
    * Para deletar uma função:
    ```
        drop funcion nome_da_funcao
    ```

### Big Data

É a coleção de conjunto de dados, grandes e complexos, que não podem ser processados por bd ou aplicações de processamento tradicionais.

4 V's:
* **Volume** (Tamanho dos dados);
* **Variedade** (Formato dos dados);
* **Velocidade** (Geração dos dados);
* **Veracidade** (Confiabilidade dos dados).

BIG DATA E CIÊNCIA DE DADOS **NÃO SÃO A MESMA COISA**:
* BIG DATA é a matéria prima;
* CIÊNCIA DE DADOS é o conjunto de técnicas para analise dos dados.

**Big Data + Ciência de dados = Big Data Analytics**

Como armazenar tantos dados?
* Dados estruturados: **Data Warehouse**;
* Dados não estruturados: **Data Lake / Data Store**.

Existem dois tipo de banco de dados:
* **Banco de Dados Relacional**- dados estruturados e com schema (organização de dados) bem definido e criado antes do armazenamento dos dados (dados organizados em tabelas)

* **Banco de Dados Não Relacional**- dados semi ou não estruturados e outros relacionamentos podem existir entre os dados, schema não definido antes do armazenamento ou definido no momento do armazenamento dos dados.

**Data Warehouse**
*  Sistema de armazenamento que conecta e harmoniza grandes quantidades de dados de diversas fontes diferentes. Armazenam dados atuais e históricos em um único lugar e atuam como fonte de informações confiáveis para a organização. Alguns benefícios do Data Warehouse são:
    * melhor Análise de negócios;
    * consultas Mais rápidas;
    * melhoria da Qualidade dos Dados;
    * visão Histórica.

**Data Lake**
* Repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala. O armazenamento dos dados pode ser efetuado da forma como estão na fonte. O schema não é definido quando os dados são capturados. O principal desafio de uma arquitetura de Data Lake é que os dados são armazenados sem supervisão, sendo necessários mecanismos definidos para catalogar e proteger os dados, evitando que se tornem um "Data Swamp". Para atender públicos mais amplos, Data Lakes precisam de governança, gestão de metadados, consistencia semântica e controles de acesso. Alguns benefícios do Data Lake são:
    * armazenamento em formato bruto;
    * importação de qualquer quantidade de dados em tempo real;
    * repositório central para todos os dados da empresa;
    * sem necessidade de movimentação dos dados.

* Importar dados para o Data Warehouse - **ETL** (Extração, Transformação e Carga)
* Importar dados para o Data Lake - **ELT** (Extração, Carga e Transformação)

**Data Hub**
* estrutura com Data Lake & Data Warehouse.

**Data Store**
* repositório para armazenar e gerenciar de forma persistente coleções de dados que incluem não apenas dados estruturados, mas também tipos de armazenamentos variados, como documentos, dados no formato de chave-valor, filas de mensagens e outros tipos de arquivos. Alguns exemplos de **Data Store**:
    * Armazenamento de chave-flor (Redis, Memcached);
    * Motor de Pesquisa de texto completo (Elastic Search);
    * Fila de Mensagens(Apache Kafka);
    * Sistema de arquivos distribuídos (Hadoop HDFS, AWS S3).

* BENEFÍCIOS DO **DATA STORE**:
    * Armazenamento de Variados Tipos de Dados;
    * Flexibilidade (armazenamento);
    * Suporte a Dados Semi-Estruturados;
    * Custo Total Menor.

**Cluster de Computadores**
*  É o conjunto de servidores com um mesmo propósito visando fornecer um tipo de serviço, como armazenamento ou processamento de dados.

**Armazenamento Paralelo**
*  É a distribuição do armazenamento de dados através de diversos servidores (computadores), o que permite aumentar consideravelmente a capacidade de armazenamento usando hardware de baixo custo.

**Apache Hadoop HDFS**
* Trata-se de um sistema de arquivos distribuido, que gerencia o armazenamento paralelo através de diversos computadores.

**Cloud Computing** 
* É a entrega de serviços de computação incluindo servidores, armazenamento, bancos de dados, rede, software, análise e inteligência pela Internet (“a nuvem”) para oferecer recursos flexíveis, inovação e economia de escala.

**Machine Learning**:
* É uma sub-área da Inteligência Artificial (IA) e da Ciência da Computação que se concentra no uso de dados e algoritmos para imitar a forma como os humanos aprendem, melhorando gradativamente sua precisão. A seguir, o pipeline do Machine Learning:
    * Preparação dos dados: os dados são separados (engenheiro de dados) e preparados (cientista de dados realiza a limpeza, transformação, normalização e processamento);
    * Construção e treinamento do Modelo: nessa etapa eles são modelados, ocorrendo a seleção de algoritmo, otimização de hiperparâmetros, treinamento e teste e avaliação. Esse é um trabalho mútuo entre o cientista de dados e engenheiro de IA;
    * Deploy do Modelo: por fim, o engenheiro de Machine Learning realiza o deploy do modelo.

* **MLOps** - conjunto de práticas para colaboração e comunicação entre Cientista de Dados e profissional de operações, um trabalho do Engenheiro de Machine Learning. Facilita o alinhamento dos modelos às necessidades do negócio e visa unificar o desenvolvimento de sistemas de ML (dev) e a implantação de sistemas de ML (ops) para padronizar e agilizar a entrega contínua de modelos de alto desempenho em produção;

* **DevOps** - abordagem para desenvolvimento de software que acelera o ciclo de vida de construção usando automação.

**VISÃO GERAL**:
* **MLOps** - operação do fluxo de trabalho em Machine Learning;
* **AIOps** - Operação do fluxo de trabalho em IA.
* **DataOps** - Conceito mais recente que abrange toda a operação de dados de uma empresa. Trata-se de uma metodologia ágil e orientada a processos para desenvolver e entregar análises, a capacidade de habilitar soluções, desenvolver produtos e ativar dados para valor comercial em todas as camadas de tecnologia, da infraestrutura à experiência do usuário final.

**BIG DATA vs SMALL DATA**:
* Big Data- grande volumes de dados, com muita variedade e gerados em alta velocidade.
* Small Data- dados que estão disponíveis em quantidade mínima suficiente para compreensão humana.

**Data as a Service** (Daas):
* Trata-se de uma estratégia de gerenciamento de dados que visa alavancar os dados como um ativo de negócios para maior agilidade no processo de análise. Concentra-se no provisionamento de dados de uma variedade de fontes sob demanda por meio do uso de APIs. Os principais benefícios de DaaS:
    * monetização de dados;
    * redução de custos;
    * caminho mais rápido para inovação;
    * agilidade no processo de decisão baseado em dados;
    * menor risco no uso de dados;
    * criação de uma cultura Data-Driven.

**ETL** (Extract, Transform, Load):
* **Extract** (Extração): Nesse estágio, os dados são coletados de várias fontes, como bancos de dados, sistemas de arquivos e APIs.
* **Transform** (Transformação): Os dados extraídos passam por processos de limpeza, conversão, agregação e manipulação para torná-los adequados para análise e armazenamento. Isso pode envolver a padronização de formatos, remoção de duplicatas e aplicação de cálculos.
* **Load** (Carregamento): Os dados transformados são carregados em um repositório de dados, como um data warehouse ou um sistema de armazenamento adequado para análises posteriores.

**ELT** (Extract, Load, Transform):
* Extract (Extração): Assim como no ETL, os dados são coletados de várias fontes.
* Load (Carregamento): Os dados extraídos são inicialmente carregados em um repositório de dados sem muita transformação.
* Transform (Transformação): A etapa de transformação ocorre após o carregamento dos dados. Aqui, os dados são transformados e preparados para análise conforme necessário. Isso pode incluir consultas complexas, agregações e processos de limpeza.

A principal diferença entre ETL e ELT é o momento em que a transformação dos dados acontece. No ETL, a transformação ocorre antes do carregamento dos dados no repositório final, enquanto no ELT, a transformação ocorre após o carregamento dos dados. A escolha entre ETL e ELT depende das necessidades específicas do projeto, das ferramentas utilizadas e das características dos dados a serem processados.


**Data Lakehouse**:
* Um Data Lakehouse é uma nova arquitetura de gerenciamento de dados que combina as vantagens de Data Lakes (flexibilidade, escalabilidade) com os recursos de gerenciamento de dados e transações ACID de Data Warehouses. Isso permite executar Business Intelligence (BI) e Machine Learning (ML) em todos os dados armazenados em um único repositório. A estrutura é construída sobre um design de sistema aberto, incorporando elementos de Data Warehouses no armazenamento de baixo custo usado em Data Lakes. Esse modelo permite maior agilidade, eliminando a necessidade de acessar múltiplos sistemas para usar os dados. Data Lakehouses asseguram que as equipes tenham acesso rápido a dados completos e atualizados para análises, ciência de dados e projetos de aprendizado de máquina.

**Data Mesh**:
* é uma abordagem de arquitetura e organização de dados que busca superar os desafios das abordagens centralizadas, como Data Warehouses e Data Lakes. Em vez de centralizar os dados, o Data Mesh descentraliza a propriedade e o gerenciamento dos dados em domínios específicos. Cada domínio é responsável por seus próprios dados, tratados como produtos, com equipes multifuncionais cuidando deles. Isso leva a uma arquitetura distribuída orientada por domínio.

* Os princípios do Data Mesh são:
    * **Descentralização orientada ao domínio**: Cada domínio é responsável por seus dados, permitindo que eles sejam tratados como produtos independentes.
    * **Dados orientados ao domínio como produtos**: Os dados são vistos como produtos, com equipes de propriedade que os gerenciam e fornecem.
    * **Infraestrutura de dados de autoatendimento**: Uma plataforma de dados de autoatendimento é fornecida para que equipes de domínio possam criar e gerenciar seus produtos de dados.
    * **Governança federada**: A governança é automatizada para permitir a interoperabilidade entre produtos de dados e a colaboração entre equipes.
* O Data Mesh busca democratizar a inovação usando dados, promovendo a descentralização, interoperabilidade e foco na experiência do consumidor de dados. É uma abordagem que atende bem a organizações com múltiplos domínios, sistemas e equipes geradoras de dados. Embora ainda haja lacunas em ferramentas comerciais, a implementação do Data Mesh está em evolução, com arquitetos e engenheiros de dados liderando essa transformação.

**Big Data Analytics**
* É o processo de examinar e interpretar grandes volumes de dados complexos, coletados de diversas fontes e em diferentes formatos. Essa análise envolve o uso de técnicas avançadas, como Machine Learning e processamento de linguagem natural, para identificar padrões, tendências e insights relevantes que não seriam facilmente perceptíveis por meio de abordagens tradicionais.
* Ao extrair informações significativas a partir desses dados, as organizações podem tomar decisões mais informadas, otimizar operações, melhorar a experiência do cliente e desenvolver estratégias competitivas.

Uso de Big Data em empresas:
* **Manufatura**: Na indústria de manufatura, o Big Data é empregado para otimizar processos, prever falhas de equipamentos, melhorar a eficiência da cadeia de suprimentos e aprimorar a qualidade do produto. Sensores e dispositivos conectados coletam dados em tempo real, permitindo a análise de fluxos de produção, identificação de gargalos e o desenvolvimento de modelos preditivos para manutenção preventiva.
* **Finanças**: No setor financeiro, o Big Data é utilizado para análise de riscos, detecção de fraudes, personalização de serviços bancários e previsões de mercado. A análise de grandes volumes de dados históricos e em tempo real ajuda a identificar padrões suspeitos em transações, ajustar modelos de crédito e oferecer recomendações personalizadas para os clientes, contribuindo para decisões mais informadas.
* **Saúde**: Na área da saúde, o Big Data é aplicado para melhorar o diagnóstico, tratamento e pesquisa médica. Análises avançadas de dados clínicos e genômicos permitem a personalização dos tratamentos, a identificação precoce de doenças e a pesquisa de medicamentos mais eficazes. Além disso, dispositivos de monitoramento remoto coletam dados em tempo real, auxiliando na gestão de pacientes crônicos.
* **Varejo**: No varejo, o Big Data é usado para compreender os padrões de compra dos clientes, otimizar a gestão de estoques, desenvolver estratégias de precificação dinâmica e melhorar a experiência do cliente. A análise de dados de vendas, preferências e comportamento do consumidor ajuda a antecipar tendências, personalizar promoções e melhorar a eficácia do marketing.

**Projeto de Big Data**
1. **Definição do Business Case**: Identificar a oportunidade de negócios que o projeto de Big Data pretende aproveitar. Analisar como os dados podem impulsionar decisões e inovações, e como isso se alinha com as metas organizacionais.
2. **Planejamento do Projeto**: Criar um plano abrangente que detalhe os objetivos, escopo, recursos, cronograma e riscos do projeto. Definir as equipes envolvidas, estabelecer marcos e definir métricas de sucesso.
3. **Definição dos Requisitos Técnicos**: Especificar as necessidades técnicas, como infraestrutura de armazenamento, processamento, ferramentas analíticas e requisitos de segurança. Garantir que a arquitetura escolhida atenda às demandas do projeto.
4. **Criação de um "Total Business Value Assessment"**: Avaliar o valor total do projeto considerando benefícios e custos. Isso envolve calcular os impactos financeiros, operacionais e estratégicos, comparando os benefícios previstos com os investimentos necessários.