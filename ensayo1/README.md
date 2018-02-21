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

**Para mas informacion**: 
http://mininet.org/walkthrough/

> **Nota**
> No se usa controlador para la programacion del switch

### Test 2

**Resumen**:
Usando containernet hacer la misma prueba anterior.

**Notas**: Por lo menos hacer lo siguiente antes de correr si el script no arranca
1. Si hay algun container corriendo este se debera eliminar ```docker stop ...```
2. Tambien es necesario correr mn -c
3. Para hacer mejor el test es necesario que la imagen a emplear tengan herramientas que permitan correr el comando ping por ejemplo.
4. Se creo un **Dockerfile** con las herramientas de red. El nombre de la imagen producida con el comando ```sudo docker build -t ubuntu_net_tools .``` fue ubuntu_net_tools. De como que se procedio a modificar las imagenes cargadas en los containers
5. A diferencia del caso tradicional con mininet, fue necesario agregar el controlador.

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

**Imagenes**:


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


# Enlaces:
* https://blog.codeship.com/the-basics-of-the-docker-run-command/
* https://www.digitalocean.com/community/tutorials/docker-explained-using-dockerfiles-to-automate-building-of-images
* https://github.com/mininet/mininet/wiki/Introduction-to-Mininet
* http://noise.gatech.edu/classes/cs8803sdn/fall2014/


