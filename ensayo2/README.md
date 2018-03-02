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

* **Contenedores**: h1, h2, cadvisor (empleado para monitoreo)

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

## Comandos utiles

`

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
