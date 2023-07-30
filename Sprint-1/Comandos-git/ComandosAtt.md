# Comandos de atualização e compartilhamento

O Git dispõe de uma série de comandos para serviços de atualização e compartilhamento com outros desenvolvedores. São eles:

* `git fetch` - com outros desenvolvedores criando novos branches, o comando atualiza com todos os branches e tags que ainda não estejam sendo reconhecido pelo sistema;
* `git remote` - adiciona um novo repositório para "trackear" ou remover. Quando usado para criar um repositório remoto, o comando é acompanhado de `add origin <linkdorepositorio>`;
* `git submodule` - verifica os submódulos (maneira de possuir dois ou mais projetos em um só repositório) atuais;
    * `git submodule add <linkdorepositorio>` - adiciona o submódulo.
    * `git push --recurse-submodules=on-demand` - envia commits para o repositório do submódulo;

---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)