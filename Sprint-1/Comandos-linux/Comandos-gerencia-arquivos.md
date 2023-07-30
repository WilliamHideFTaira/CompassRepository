# Comandos de gerencia de arquivos

O Linux dispõe de diversos comandos para gerenciar aquivos. São eles:

* `cd` - muda de diretório:
    * `cd /diretório/` - mudança direta de diretórios;
    * `cd diretorio` - mudança entre diretórios próximos;
    * `cd --` - volta para diretório anterior;
    * `cd ..` - entra no diretório pai do atual;
    * `cd ../../` - move dois diretórios acima do atual (mais `../` aumenta a movimentação);
    * `cd -` - mostra último diretório antes do atual;
    * `cd ~` - move para home do usuário atual;
    * `cd ../diretorio/` - volta e avança em outro diretório;
    * `cd ../ && ls` - muda de diretório e utiliza outro comando;
* `ls` - lista arquivos e diretórios:
    * `ls -l` - lista arquivos e diretórios com detalhes;
    * `ls -a` - lista arquivos ocultos;
    * `ls -lh` - mostra tamanho dos arquivos em formato human readable (ex: 4 kb, 8Mb);
    * `ls -ltr` - mostra data da ultima modificação;
    * `ls -l /etc` - lista arquivos em outro diretório;
    * `ls -r` - lista arquivos e diretórios em ordem reversa;
    * `ls -R` - mostra subdiretórios;
    * `ls - lS` ou `ls -lSh` - ordena por tamanho do arquivo;
    * `ls -m` - lista os arquivos separados por vírgula;
    * `ls -help` - mais informações;
* `clear` - limpa a tela do terminal;
* `cat` - mostra o conteúdo de um arquivo;
    * `cat file1 file2` - mostra o conteúdo de múltiplos arquivos;
    * `cat > file.txt` - cria arquivo;
    * `cat -n file` - mostra o número de linhas do arquivo;
    * `cat -e file` - mostrando $ em todo final de linha;
    * `cat file1 > file2` - cria um arquivo por meio de outro;
    * `cat file1 >> file2` - adiciona conteúdo a um arquivo a partir de outro;
    * `cat file1 file2 > file3` - adiciona conteúdo de múltiplos arquivos em apenas um;
* `touch` - cria ou muda a data de acesso de um arquivo;
    * `touch file` - alterando data ou criando arquivo (adicione mais files como parâmetro para criar mais);
* `man` - comando do manual do sistema operacional (ex: `man ls` ou  `man cd`);
* `mkdir` - cria um diretório:
    * `mkdir dir1 dir2 dir3` - cria vários diretórios;
    * `mkdir -v dir1 dir2 dir3` - cria diretórios com verbose (mensagem informativa);
    * `mkdir -p dir1/dir2/dir3` - cria estrutura de diretórios;
* `rm` - deleta diretório ou arquivo:
    * `rm a.txt` - remove arquivo (adicione mais arquivos como parâmetro para removê-los também);
    * `rm -i a.txt` - remove arquivo com interatividade (sistema solicita confirmação para remover);
    * `rm -f a.txt` - força remoção de arquivo;
    * `rm -dv dir` - remove diretório;
    * `rm -rfv dir` - remove diretórios e arquivos recursivos (não solicita confirmações);
    * `rmdir dir` - deleta diretório vazio;
    * `rmdir -r dir/dir2/dir3` - deleta diretórios varios;
* `cp` - copia arquivos e diretórios:
    * `cp texte.txt texte2.txt` - copia um arquivo;
    * `cp texte.txt dir/texte.txt` - copia um arquivo para outro diretório;
    * `cp a.txt b.txt c.txt dir` - copia vários arquivos em um diretório;
    * `cp -r dir1 dir2` - copia diretórios de forma recursiva;
    * `cp dir1/* dir2` - copia todos os arquivos de um diretório para outro;
    * `texte* dir` - copia todos os arquivos x para um diretório;
* `mv` - move diretórios e arquivos:
    * `mv a.txt b.txt` - move um arquivo;
    * `mv teste.txt dir/teste.txt` - move um arquivo para um diretório;
    * `mv * dir/` - move vários arquivos para um diretório;
---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)