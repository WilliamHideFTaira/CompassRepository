# Sprint 8

Arquivo README.md para resumir a execução da camada Lambda

## Configurações da Função

* Tempo de execução: Python 3.7
* Memória: 1024MB
* Armazenamento Temporário: 1024MB
* Tempo Limite: 15 minutos
* Permissões: AmazonS3FullAccess (adicionada) / AWSLambdaBasicExecutionRole-a3b03073-ed74-44bc-a08f-3a50358584e3 (padrão)
* Variáveis de ambiente: foi criada a variável de ambiente "chaveAPI" com o valor da chave api para garantir a segurança dos dados

## Execução da camada Lambda

A criação da camada foi feita a partir do passo a passo da Sprint 6 - AWS Lambda, usando um dockerfile e comandos para execução:
### 1: Dockerfile e execução
Segue adiante o dockerfile que foi utilizado:
```
FROM amazonlinux:2.0.20200602.0
RUN yum update -y
RUN yum install -y \
python3-pip \
zip \
RUN yum -y clean all
RUN python3.7 -m pip install --upgrade pip
```

Os comandos utilizados para a execução do docker foram:

```
$ docker build -t amazonlinuxpython37 .
$ docker run -it amazonlinuxpython37 bash
```


### 2: Configuração da camada

Comandos shell para instalação das bibliotecas necessárias:
```
bash-4.2# cd ~  
bash-4.2# mkdir layer_dir
bash-4.2# cd layer_dir/
bash-4.2# mkdir python
bash-4.2# cd python/
```

Logo depois, o comando para instalação das bibliotecas (versão do urllib3 precisou ser especificada para funcionamento apropriado da camada)
```
bash-4.2# pip install requests pandas urllib3==1.26.6 -t .
```

O último comando usado foi para colocar o conteúdo em um arquivo .zip
```
zip -r minha-camada-pandas.zip .
```


### 3: Arquivo .zip e upload da camada

Em outro terminal, o arquivo .zip foi copiado para a pasta em questão e preparado para ser enviado a um bucket S3 específico para o uso da camada:

```
docker cp efb2:/root/layer_dir/minha-camada-pandas.zip ./
```
