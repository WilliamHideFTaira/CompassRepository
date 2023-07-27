# Comandos Fundamentais

O Git dispõe de uma série de comandos para uma boa gestão de um repositório. São eles:

* `git init` - cria um novo projeto no git;
* `git clone URL` - clona um repositório **remoto** na pasta, criando um repositório **local**;
* `git status` - verifica alterações no projeto **local**;
* `git add` - adiciona arquivos novos ao projeto **local**;
* `git commit` - envia alterações para o repositório **local**. Uma boa prática é adicionar uma mensagem junto ao commit, usando `-m "mensagem"` para manter o gerenciamento do projeto;
* `git push` - envia alterações do repositório **local** para o repositório **remoto**;
* `git pull` - sincroniza o repositório **local** com o **remoto**;
* `git rm` - remove um arquivo da monitoração do git. Caso queira adicioná-lo novamente, use `git add`;
* `git log` - verifica o histórico de alterações do repositório;
* `git mv` - move ou altera o nome de um arquivo no repositório **local**;
* `git checkout` - retorna um arquivo modificado no repositório **local** ao seu estado original ou [troca de branch](Sprint-1/Comandos-branches);
* `git reset` - reinicia todas as mudanças feitas no repositório **local**. Isso aplica-se em commits e adds realizados antes do `pull`.
* `git stash` - salva alterações atuais em um **stash** e reseta alterações do repositório **local**;
    * `git stash list` - lista stashs criadas;
    * `git stash nomedastash` - recupera as alterações de uma stash;
    * `git stash clear` - limpa totalmente as stash de um [branch](Sprint-1/Comandos-branches); 
    * `git stash drop nomedastash` -  exclui uma stash específica;

É possível também fazer ignorar arquivos no projeto, adicionando um arquivo chamado .gitignore e inserindo nele o nome de todos os arquivos a serem ignorados (útil para arquivos gerados automaticamente ou arquivos com informações sensíveis).