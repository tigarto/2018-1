# COMANDOS:
# 1. Para crear la imagen
#    
#             sudo docker build -t [name] .
#
#    Ejemplo:
#    sudo docker build -t ubuntu_net_tools .
#
# 2. Para correr un container a partir de la imagen
#   
#             sudo docker run -name [instanceName] -i -t [name]
#              sudo docker images
#
#    Ejemplo:
#    sudo docker run -name ubuntu1 -i -t ubuntu_net_tools


# Imagen base
ARG  CODE_VERSION=latest
ARG  base=ubuntu
FROM ${base}:${CODE_VERSION}

# Herramientas adicionales a instalar
RUN apt-get update
RUN apt-get install -y net-tools
RUN apt-get install -y mtr-tiny traceroute netcat dnsutils curl

# Instruccion a ejecutar
CMD bash
