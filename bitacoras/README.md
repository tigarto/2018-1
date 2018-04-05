# Bitacoras de test

> **URL seguimiento**: https://github.com/sonata-nfv/son-install/issues/159

## Fecha: 04/04/2018

Siguiento la recomendacion de **arocha7** se procedio a hacer lo que dijo:
1. overload the "sp_ver" parameter in the command line, like:

```
sudo ansible-playbook utils/deploy/sp.yml -e "target=localhost plat=sp sp_ver=latest" -v --limit @/home/ubuntu/son-install/utils/deploy/sp.retry
```

Vamos a ejecutar el comando tal y como se sugiere en las siguientes paginas:
* https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file
* https://stackoverflow.com/questions/418896/how-to-redirect-output-to-a-file-and-stdout


2. change 'sp_ver' in the Role's defaults file to "latest":

vi roles/sp/defaults/main.yml
sp_ver: latest

http://www.googlinux.com/list-all-tags-of-docker-image/
https://stackoverflow.com/questions/28320134/how-to-list-all-tags-for-a-docker-image-on-a-remote-registry
