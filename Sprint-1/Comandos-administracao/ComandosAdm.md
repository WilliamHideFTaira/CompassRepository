# Comandos de administração do repositório

O Git dispõe de uma série de comandos para auxiliar a administração do repositório, com limpezas e otimização. São eles:

* `git clean` - verifica e limpa arquivos que não estão sendo mais "trackeados" (todos os arquivos fora do "add"). Mais utilizado para arquivos que são gerados automaticamente;
* `git gc` - da abreviação **Garbage Collector**, identifica arquivos que não são mais necessários e os exclui, melhorando a performance;
* `git fsck` - da abreviação **File System ChecK**, verifica a integridade dos arquivos, garantindo que nenhum esteja corrompido;
* `git reflog` - mapeia **todos** os passos no repositório, desde commits até mudança de branch. Ficam salvos até expirar (padrão: 30 dias);
* `git archive --format zip --output master_files.zip master` - transforma o repositório em um arquivo compactado;
---
###### [VOLTAR](https://github.com/WilliamHideFTaira/CompassRepository/Sprint-1/)