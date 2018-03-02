# ENSAYOS PRELIMINARES - ENSAYO 2

**Fecha**: 01/03/2018

## Objetivos

> 1. Correr containers y itoreandolos con cAdvisor.
> 2. Mirar los resultados de la red.
> 3. Recordar comandos de manipulacion

## Sobre los containters

### Descripcion breve
Se van a manejar varios contenedores que van a servir como hosts, asi mismo se va a agregar un contenedor conocido como cAdvisor que sera el encargado de realizar el sensado de los contenedores en funcionamiendo. En cada caso se describiran los contenedores en prueba.


### Caso 1: 

### Contenedores

Los contenedores que se ejecutan son:
* h1
* h2
* cadvisor (empleado para monitoreo)

**h1**

```
sudo docker run \
  --rm \
  --name=h1 \
  --hostname h1 \
  -ti ubuntu:trusty /bin/bash
```

**h2**

```
sudo docker run \
  --rm \
  --name=h2 \
  --hostname h2 \
  -ti ubuntu:trusty /bin/bash
```

**cAdvisor**

```
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
```

### Verificando la red

```
sudo docker network ls
sudo docker network inspect bridge
```

Del ultimo comando se observo que los containers estan conectados a la misma red con las siguiente IPs:

| Container  | Second Header |
| ------------- | ------------- |
| h1  | 172.17.0.2  |
| h2  | 172.17.0.3  |
| cadvisor  | 172.17.0.4  |

### Monitoreando los containers

Una vez cAdvisor esta corriendo lo que se hace es colocar la siguiente URL en el navegador: localhost:8080, una vez hecho esto se podra observar toda la informacion asociada.

### Preguntas:

#### Pregunta 1  
¿Si se coloco un container conectado a host y no a bridge (opcion por defecto), aparecera en cAdvisor?

```
sudo docker run \
  --rm \
  --network=host \
  --name=h_net_host \
  --hostname h_net_host \
  -ti ubuntu:trusty /bin/bash
```

**Respuesta**: Si

#### Pregunta 2 
¿Si se coloco un container conectado a none y no a bridge (opcion por defecto), aparecera en cAdvisor?

```
sudo docker run \
  --rm \
  --network=none \
  --name=h_none_host \
  --hostname h_none_host \
  -ti ubuntu:trusty /bin/bash
```

**Respuesta**: Si


#### Pregunta 3

Si creo otra red nueva, tipo bridge, distinta de donde esta cAdvisor y concecto aqui el nuevo container se ve en cAdvisor?  

Se creo la red **my-net**:
```
docker network create my-net
sudo docker network ls
```

Se creo el container y se engancho a esta nueva red:

```
sudo docker run \
  --rm \
  --network=my-net \
  --name=h_my-net_host \
  --hostname h_my-net_host \
  -ti ubuntu:trusty /bin/bash
```

Aun se seguia viendo en el cadvisor por lo que se elimino.

```
sudo docker network inspect my-red
sudo docker network ls
docker network rm my-red
```

**Respuesta**: Si

## Comandos utiles

> **Para containers**
> 1. sudo docker images
> 2. sudo docker containers ls
>
> **Para redes**
> 1. sudo docker network ls
> 2. docker network inspect RED
> 3. docker network create RED
> 4. docker network rm RED

## Referencias
 
* [Monitoring and debugging using an SDK for NFV-powered telecom applications](https://biblio.ugent.be/publication/8521281/file/8521284.pdf)
* [Monitoring Docker Containers – docker stats, cAdvisor, Universal Control Plane](https://blog.couchbase.com/monitoring-docker-containers-docker-stats-cadvisor-universal-control-plane/)
* [Monitoring Docker Swarm with cAdvisor, InfluxDB and Grafana](tps://botleg.com/stories/monitoring-docker-swarm-with-cadvisor-influxdb-and-grafana/)
* [How to setup Docker Monitoring](https://www.brianchristner.io/how-to-setup-docker-monitoring/)
* [Comparing 10 Container Monitoring Solutions for Rancher](http://rancher.com/comparing-10-container-monitoring-solutions-rancher/)
* [DockOne's Sharing (12th): Kubernetes's Exploration Practice in Micro-Service](http://www.dockermall.com/dockones-sharing-12th-kubernetess-exploration-practice-in-micro-service/)
* [Why We Need DevOps & Top 10 Things To Know in DevOps](https://www.xenonstack.com/blog/devops/top-10-things-to-know-in-devops)
* [List of Best Docker Container Clustering and Orchestration Tools/Services](https://devopscube.com/docker-container-clustering-tools/)
* https://docs.docker.com/network/bridge/#manage-a-user-defined-bridge
