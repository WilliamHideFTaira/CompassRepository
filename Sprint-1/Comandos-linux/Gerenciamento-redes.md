# Gerenciamento de redes

##### Como funciona?

O sistema web funciona de forma bem simples:
1. Envio de requisição para domínio (DNS);
2. Verificação do domínio (DNS = IP);
3. Requisição da resposta para o servidor que pertence a esse domínio;
4. Retorno da resposta a quem requisitou;

##### DNS
Sigla para Domain Name System, é graças a ele que não precisamos gravar endereços de IP, pois ele faz a tradução do endereço em um domínio;

##### Portas

É um endpoint, sempre associada a um IP.

##### TCP

Sigla para Transmission Control Protocol, é o protocolo utilizado para transmissão de dados pela rede (ex: HTTPS é o protocolo para navegar na internet; SMTP é o protocolo para envio de emails).

##### UDP

Sigla para User Datagram Protocol, é parecido com o TCP, mais focado na velocidade do envio do que na sua segurança (usado muito em jogos online).

### Comandos de verificação de rede

Alguns comandos que auxiliam no gerenciamento da rede são:

* `ping www.google.com` - envia um sinal para um domínio para testar tempo de resposta e conexão
* `sudo apt-get install net-tools` - **instala netstat no Linux para comandos abaixo**:
    * `netstat -a` - mostra todas as conexões UDP e TCP ativas:
        * `netstat -at` - mostra apenas conexões TCP ativas;
        * `netstat -au` - mostra apenas conexões UDP ativas;
* `ipconfig -a` - exibe informações detalhadas da conexão;
* `ipconfig eth0` - verifica redes específicas;
* `nslookup google.com` - consulta servidores de nomes para obter informações de domínio;
* `sudo tcpdump` - captura todo o tráfego na interface de rede padrão;
---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)