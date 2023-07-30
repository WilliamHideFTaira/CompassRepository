# Comandos de gerencia de pacotes

O Linux dispõe de diversos comandos para gerenciar pacotes do sistema. São eles:

* `sudo apt-get update` - verifica novas atualizações e atualiza repositórios, mas **não instala nada novo**(`sudo` = superuser do, comando para permitir usuários executarem tarefas administrativas);
* `sudo apt-get upgrade` - depois do comando `update`, esse comando instala as atualizações dos pacotes;
* `sudo apt-get install tree` - instala um pacote `tree`;
* `sudo apt-get purge tree` - remove um pacote `tree`;
* `sudo apt-get dist-upgrade` - atualiza o Linux, instalando pacotes de última versão, removendo os que não são mais utilizados;
* `sudo apt-get autoremove` - remove pacotes não utilizados;
* `apt-cache search package` - busca pacotes;
---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)