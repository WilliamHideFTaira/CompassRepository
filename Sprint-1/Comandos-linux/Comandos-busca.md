# Comandos de gerencia de busca em arquivos

O Linux dispõe de diversos comandos para fazer buscas em arquivos e diretórios, tornando-as mais inteligentes. São eles:

* `head file` - lê o topo de um arquivo (adicionar mais arquivos no parâmetro realiza a leitura de mais arquivos):
    * `head -n15 file` - lê um determinado número de linhas (no caso, 15);
    * `head file > file2` - copia o resultado do head de um arquivo em outro;
* `tail file` - lê o final de um arquivo (adicionar mais arquivos no parâmetro realiza a leitura de mais arquivos):
    * `tail -n15 file` - lê um determinado número de linhas (baixo para cima);
    * `tail file1 > file2` - copia o resultado do tail de um arquivo em outro;
    * `tail -f file` - monitora em tempo real as últimas linhas de um arquivo;
* `grep 'word' file` - busca palavra em um arquivo:
    * `grep -i 'word' file` - ignora case sensitive;
    * `grep -r 'word' file` - busca de forma recursiva;
    * `grep -c 'word' file` - conta ocorrência de palavra no arquivo;
* `find . -name 'teste*'` - encontra arquivos pelo nome:
    * `find . -iname 'TESTE.txt'` - ignora case sensitive;
    * `find . -empty` - procura arquivos **vazios**;
    * `find . -type f` - busca **arquivo** por tipo;
    * `fint . -type d` - busca **diretório**;
* `locate file` - localiza um arquivo (igual ao find, mas com mais performance, por armazenar os dados em um banco de dados):
    * `locate .html -n 10` - localiza arquivo com **máximo** de itens;
    * `locate -S` - ver status do banco de dados;

---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)