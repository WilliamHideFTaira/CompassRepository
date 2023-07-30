# Comandos de gêrencia de usuários

O Linux dispõe de diversos comandos para gerenciar usuários do sistema. São eles:

* `adduser user` - cria usuário;
* `userdel --remove user` - remove usuário;
* `usermod -c 'newname' oldname` - modifica nome de usuário;
* `usermod -L user` - desabilita usuário;
* `usermod -U user` - habilita usuário;
* `getent group` - ver grupos (grupo de usuários, facilitando gerenciar permissões);
* `groupadd group` - cria grupo;
* `groupdel group` - deleta grupo;
* `sudo usermod -a -G group user` - muda usuário de grupo;
* `sudo gpasswd -d user group` - remove usuário de grupo;
* `sudo su` - acessa o **root** (permissões de superusuário);
* `passwd` - muda a senha.
---
#### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/tree/main/Sprint-1)