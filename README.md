SlkFormat
=========

Formatador para Slackware Linux

Instalação:

1 - Edite ou crie o arquivo /etc/bash.bashrc
2 - Insira a seguinte linha nele: alias plugdev="ls -l /dev | grep 'plugdev' | awk -F' ' '{print \$10}'"
3- Salve o arquivo e de permissão de execução a ele: chmod +x /etc/bash.bashrc
