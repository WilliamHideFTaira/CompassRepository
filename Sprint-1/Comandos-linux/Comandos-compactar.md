# Comandos para compactar e descompactar arquivos no Linux

O Linux dispõe de alguns comandos para compactar e descompactar arquivos pelo próprio terminal. São eles:

* `tar -czvf name-of-archive.tag.gz /path/to/directory-of-file` - compacta arquivo de acordo com parâmetros:
    * `c` - criar arquivo;
    * `z` - comprime arquivo;
    * `v` - mostra progresso;
    * `f` - especifica nome do arquivo;\
Obs: é possivel compactar múltiplos diretórios e arquivos inserindo mais parâmetros no final do comando.

* `tar -xzvf archive.tar.gz` - descompacta arquivo:
    * `tar -xzvf archive.tar.gz -C /tmp` -descompacta em local específico.
* `zip -r nome_do_arquivo.zip diretório_ou_arquivo` - compacta em zip;
* `unzip nome_do_arquivo.zip -d destino` - descompacta em zip.
---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)