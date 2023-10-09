# Resumo Sprint 6
Este readme.md descreve as principais etapas e realizações da Sprint. O projeto envolveu a criação de um site, manipulação de dados, uso do Docker e integração com o Amazon S3 e AWS Lambda.

## Criação do Bucket S3 - bucket-will
Para iniciar o projeto, foi criado um bucket S3 chamado "bucket-will". Dentro deste bucket, foram inseridos dois arquivos:

index.html: Este arquivo foi utilizado como página inicial do site e estava configurado corretamente para funcionar como esperado.

nomes.csv: Este arquivo continha dados relevantes para o projeto e foi utilizado na tabela de dados e na manipulação subsequente.

## Tabela de Dados e Análise
Foi criada uma tabela de dados funcional, na qual os dados do arquivo nomes.csv foram carregados e manipulados com sucesso. Além disso, a funcionalidade de busca pelos três nomes que mais venderam por década desde 1950 foi implementada com sucesso.

## Uso do Docker
Um Dockerfile foi criado em uma máquina virtual Linux. Nesse ambiente, a biblioteca Pandas foi adicionada e utilizada para a extração de dados do arquivo nomes.csv. Infelizmente, devido a um erro na máquina virtual, todos os comandos realizados foram perdidos e não estão disponíveis em forma de prints ou registros. No entanto, a extração de dados foi bem-sucedida e os dados foram adicionados ao bucket S3 "bucket-will".

Adicionalmente, o arquivo .zip foi adicionado, e o laboratório Lambda foi configurado com sucesso, usando 1024MB de memória e 1 minuto de tempo de execução para testes.

## Deleção de Arquivos
Por fim, todos os arquivos restantes foram deletados corretamente, garantindo uma limpeza eficaz após a conclusão do projeto.
