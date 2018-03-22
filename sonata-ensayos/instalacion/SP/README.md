# Instalacion de la SP (Service platform) de sonata

> **Nota**:
> En esta sección lo que se hace es describir de manera consisa y bajo la experiencia tenida el proceso llevado a cabo al instalar la **SP de sonata**. El documento en el cual se encuentran es la [guia de uso de sonata](http://sonata-nfv.eu/sites/default/files/sonata/public/content-files/pages/SONATA_3.0_TUTORIAL_v0.3.pdf). Este documento no pretende ser un reemplazo sino un documento que recoja de alguna manera la experiencia que se tuvo al seguir la guia de usario.


## Suposiciones:
1. Se cumplen los requisitos de hardware
2. Ubuntu Xenial 16.04
3. El Ubuntu esta limpio (es decir, es la primera vez que se lleva a cabo la instalacion de sonata)
4. Directorio de instalacion de sonata **son-install**. 

## Proceso de instalacion:
1. **Haciendo unas configuraciones preliminares**:
Mirando la seccion 4.2.2 de la guia de usuario. Antes de empezar lo unico que se hizo fue modificar la contraseña de usuario que se encuentra dentro de archivo *roles/sp/defaults/main.yml* dentro del directorio **son-install** cambiando la clave asociada al usuario creado por son-install:

**Parte antes de llevar a cabo la aplicacion del comando de instalacion**

```
sudo apt-get install -y software-properties-common
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible
sudo apt-get install -y git
git clone https://github.com/sonata-nfv/son-install.git
cd son-install
echo sonata | tee ~/.ssh/.vault_pass
```
En nuestro caso particular el comando ```echo sonata | tee ~/.ssh/.vault_pass``` saco problema asi que lo que se hizo fue crear el directorio ```.ssh``` en la carpeta ```~``` asociada al usuario y una vez alli crear el archivo ```.vault_pass``` con un editor de texto colocando ```sonata``` como contenido. Asi:

```
mkdir ~/.ssh
gedit ~/.ssh/.vault_pass
# Editar el archivo...
```
Una parte del contenido del archivo quedo asi:

```
...
# SONATA SP User created by son-install
sp_user: sonata
sp_pass: "XXXXXXXXX"
```

**Nota**: 
1. Seguramente puedo cambiar mas cosas, pero lo que se queria era evitar la contraseña larguisima ```$1$SRc2ws2Z$rSdCC/UKiatagNdfsTVuf0``` que viene por defecto.
2. Puede que no hubiera sido necesario pero despues de varios intentos de instalacion y tener problemas con el acceso quisimos hacer eso. En todo caso, podemos decir que esto lo hicimos por curarnos en salud.


2. **Corriendo el proceso de instalacion**:
Para el caso, ya se han ejecutado algunos comandos de los que se mostraron en la seccion 4.2.3 de la guia (o tambien en el siguiente [enlace](https://github.com/sonata-nfv/son-install/wiki/SONATA-SP-Installation-v3.0)), lo que sigue consiste en el resto para completar la instalacion:

El siguiente paso consistió en averiguar la IP:

```
ifconfig
br-07b3c99daecf Link encap:Ethernet  HWaddr 02:42:c7:05:5a:f3  
          inet addr:172.20.1.1  Bcast:0.0.0.0  Mask:255.255.255.0
          inet6 addr: fe80::42:c7ff:fe05:5af3/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:49 errors:0 dropped:0 overruns:0 frame:0
          TX packets:74 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:1372 (1.3 KB)  TX bytes:9716 (9.7 KB)

docker0   Link encap:Ethernet  HWaddr 02:42:05:d4:83:c2  
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::42:5ff:fed4:83c2/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:329 errors:0 dropped:0 overruns:0 frame:0
          TX packets:391 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:258636 (258.6 KB)  TX bytes:93327 (93.3 KB)
enp1s0    Link encap:Ethernet  HWaddr 68:f7:28:83:7d:a8  
          inet addr:172.21.30.124  Bcast:172.21.255.255  Mask:255.255.0.0
          inet6 addr: fe80::b3c1:d16b:4f80:174d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2157045 errors:0 dropped:0 overruns:0 frame:0
          TX packets:123223 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:547181378 (547.1 MB)  TX bytes:14598848 (14.5 MB)

...

```

Con esto aplicamos el comando:

```
sudo ansible-playbook utils/deploy/sp.yml -e "target=localhost public_ip=<your_ip4_address> sp_ver=3.0" -v
```

Donde ```<your_ip4_address>=172.20.1.1``` para nuestro caso. Una vez se sigue con la instalacion. Si todo sale bien, al final se tendra una salida como la siguiente (solo se toma un trozo de esta):

```
...
TASK [sp : Creating SONATA Service] ********************************************
changed: [localhost] => {"changed": true, "checksum": "69aab73652afb53b2ce7599c0ca94da739137cdf", "dest": "/etc/init.d/sonata", "gid": 0, "group": "root", "md5sum": "a8638487bc63a3c174e580e8d2a15b94", "mode": "0744", "owner": "root", "size": 6045, "src": "/home/tigarto/.ansible/tmp/ansible-tmp-1521590888.84-144227930714269/source", "state": "file", "uid": 0}

PLAY RECAP *********************************************************************
localhost                  : ok=104  changed=55   unreachable=0    failed=0   
```

Solo resta probar la instalacion ejecutando el siguiente comando:

```
sudo /etc/init.d/sonata status
```

El siguiente [video](https://asciinema.org/a/44MwPYliuOxxYBFkkm7M8eqM4) brindado por los creadores el proyecto resalta el proceso completo anteriormente descrito.

## Notas:
1. Se intento borrar y reinstalar, se tuvieron un sin numero de problemas, ojala esto quede listo con una instalacion y ya, basicamente se tuvieron que eliminar un monton de herramientas que ya se tenia, molestar con rutas.

