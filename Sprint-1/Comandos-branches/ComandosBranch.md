# Comandos para Branches

O Git dispõe de uma série de comandos para uma boa gestão de versões diferentes do projeto (branches). São eles:

* `git branch` - visualiza os branches disponíveis;
    * `git branch nomedabranch` - cria uma nova branch no repositório **local**;
    * `git branch -d nomedabranch` - exclui uma branch do repositório **local**;
* `git checkout nomedabranch` - muda o branch no qual está trabalhando (**pode acabar levando alterações não-commitadas, cuidado**);
* `git merge` - une dois branches, recebendo atualizações de outros desenvolvedores;
* `git tag` - cria um "checkpoint" de um branch, usado para demarcar estágios do desenvolvimento de algum recurso;
    * `git show nomedatag` - verifica uma tag;
    * `git checkout nomedatag` - muda de tag;
    * `git push origin nomedatag` - envia a tag para o repositório **remoto**, sendo assim compartilhada entre os desenvolvedores;
        * ´git push origin --tags´ - envia mais tags para o repositório **remoto**;

---
###### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/Sprint-1)