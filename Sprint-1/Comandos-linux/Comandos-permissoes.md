# Comandos de gerencia de permissões

Os usuários podem executar três ações nos arquivos:

1. Leitura (R - Read);
2. Escrita (W - Write);
3. Execução (X - Execute);

Essas permissões são divididas em 3 grupos:
1. Dono (usuário que criou diretório/arquivo);
2. Grupo (grupo de usuários ao qual o arquivo/diretório pertence);
3. Outros (outros usuários do sistema).

As permissões são representadas por dígitos numéricos, onde cada dígito é uma soma das permissões. Cada permissão tem um valor numérico atribuído:

* _0_: nenhuma permissão;
* _1_: permissão de execução;
* _2_: permissão de gravação;
* _4_: permissão de leitura;

Os dígitos numéricos são combinados e somados para representar as permissões dos três grupos em sequência. Exemplo:

* 777 - dono, grupo e outros tem permissão para ler, escrever e executar o arquivo (7 = _1_ + _2_ + _4_);

* 644 - dono tem permissão de ler e gravar no arquivo, enquanto grupo e outros tem permissão apenas para leitura(6 = _2_ + _4_ | 4 = _4_).

O Linux dispõe de diversos comandos para alterar permissões de usuários. São eles:

* `chmod xxx file/dir` - comando para alterar permissões;
* `chmod args file/dir` - comando para alterar permissões por argumento:
    * `+` - adiciona permissão a um arquivo/diretório;
    * `-` - remove permissão a um arquivo/diretório;
    * `=` - determina permissões, substituindo anteriores;
    * `u` - dono do arquivo;
    * `g` - grupo;
    * `o` - outros;
    * `a` - todos;
* `chown user file` - altera propriedade do arquivo/diretório, podendo transferir para outro usuário;
* `chown user:group file` - altera usuário e grupo do arquivo/diretório;
* `chgrp group file` - altera grupo do arquivo/diretório;
---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)