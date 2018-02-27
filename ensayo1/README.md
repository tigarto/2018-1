# ENSAYOS PRELIMINARES

## TESTS

### Test 1

**Resumen**:
Usando mininet montar una topologia sencilla de 3 host conectados de manera simple.

**Archivo**: simple_topo.py 

**Topologia montada empleando mininet**:
```
h1 --- s1 --- h3
       |
       |
       h2
```

**Uso**:

```
sudo mn --custom simple_topo.py --topo mytopo 
```
**URL**: https://github.com/tigarto/2018-1/tree/master/ensayo1/test1

**Para mas informacion**: 
http://mininet.org/walkthrough/

> **Nota**
> No se usa controlador para la programacion del switch

### Test 2

**Resumen**:
Usando containernet hacer la misma prueba anterior.

> **Notas**: Por lo menos hacer lo siguiente antes de correr si el script no arranca
> 1. Si hay algun container corriendo este se debera eliminar ```docker stop ...```
> 2. Tambien es necesario correr mn -c
> 3. Para hacer mejor el test es necesario que la imagen a emplear tengan herramientas que permitan correr el comando ping por ejemplo.
> 4. Se creo un **Dockerfile** con las herramientas de red. El nombre de la imagen producida con el comando ```sudo docker build -t ubuntu_net_tools .``` fue **ubuntu_net_tools**. De como que se procedio a modificar las imagenes cargadas en los containers, el anterior comando debe ser ejecutado previo a la simulacion si la imagen **ubuntu_net_tools** no ha sido creada.
> 5. A diferencia del caso tradicional con mininet, fue necesario agregar el controlador.

**Topologia montada empleando containernet**:

```
       c0
       |
       |
h1 --- s1 --- h3
       |
       |
       h2
```

**Uso**:

```
sudo python simple_topo_containers.py  
```

**Imagenes**:

Todos los 3 host (h1, h2 y h3) usan containers cuyas imagenes provienen del [Dockerfile](https://github.com/tigarto/2018-1/blob/master/ensayo1/Dockerfile) el cual esta basado en ubuntu pero que tiene instaladas herramientas de red para poder hacer pruebas como el ping. La imagen se puede encontrar como ubuntu_net_tools cuando se digita el comando ```sudo docker images```. 

**URL**: https://github.com/tigarto/2018-1/tree/master/ensayo1/test2

### Test 3

**Aspectos previos**
1. Verificar que se tiene instalado el controlador POX en la maquina, si no es asi en el siguiente [enlace](http://networkstatic.net/pox-openflow-controller-installation-screencast/) se brinda informacion muy util para dicha tarea, en todo caso, esto puede reducirse a los siguientes dos comandos:

```
cd $HOME
git clone http://github.com/noxrepo/pox
```

**Resumen**:
Usando mininet montar una topologia sencilla de 3 host conectados a un mismo switch. Esta red usara POX (el cual funcionara como switch) como controlador. Para el caso, como la topologia es bastante sencilla se describen las 3 formas como se llevo a cabo la acción.
1. **Forma 1**: Por medio de linea de comandos para arrancar la topologia y el controlador.
2. **Forma 2**: Llamando un script para la topologia y corriendo un controlador externo.
3. **Forma 3**: Corriendo en linea de comandos tanto la topologia como el controlador.

**Topologia montada empleando mininet**:

```
       c0
       |
       |
h1 --- s1 --- h3
       |
       |
       h2
```


**Archivo**: simple_topo.py 




**Algunos comandos de test en containernet>**:
```
nodes
net
xterm h1
xterm h2
xterm h3
# Con los contenedores con herramientas de red instaladas si dan comandos como los mostrados abajo
pingall
h1 ping -c 2 h2
```


**Comandos docker a la mano**:

```
# Comandos variados
sudo docker images
sudo docker ps -a

# One liner to stop / remove all of Docker containers
docker stop $(docker ps -a -q)
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)

# corriendo consola de un container
docker --hostname h1 --name ubuntu_container run -it ubuntu bash

# Removiendo un nombre de un container
docker rm containerName
```



## Enlaces:
* http://csie.nqu.edu.tw/smallko/sdn/sdn.htm
* http://noise.gatech.edu/classes/cs8803sdn/fall2014/
* http://noise.gatech.edu/classes/cs8001-sdn/fall2013/
* https://ee.stanford.edu/research/software-defined-networking
* https://blog.codeship.com/the-basics-of-the-docker-run-command/
* https://www.digitalocean.com/community/tutorials/docker-explained-using-dockerfiles-to-automate-building-of-images
* https://github.com/mininet/mininet/wiki/Introduction-to-Mininet
* http://noise.gatech.edu/classes/cs8803sdn/fall2014/
* https://libraries.io/github/esbrito/NFVClickNet
* https://github.com/sonata-nfv/son-tutorials/tree/master/upb-containernet-emulator-summerschool-demo
* http://sonata-nfv.eu/
* https://github.com/sonata-nfv/son-emu
* https://github.com/sonata-nfv/son-emu/wiki
* https://github.com/sonata-nfv/son-emu/wiki/Build-and-installation


