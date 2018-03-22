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

```
# SONATA SP User created by son-install
sp_user: sonata
sp_pass: "XXXXXXXXX"
```

**Nota**: Seguramente puedo cambiar mas cosas, pero lo que se queria era evitar la contraseña larguisima ```$1$SRc2ws2Z$rSdCC/UKiatagNdfsTVuf0``` que viene por defecto.

Lo demas se dejo quieto.

2. **Corriendo el proceso de instalacion**:
Tal y como se describe en la seccion 4.2.3 de la guia (o tambien en el siguiente [enlace](https://github.com/sonata-nfv/son-install/wiki/SONATA-SP-Installation-v3.0)) se procedieron a ejecutar los comandos aqui mencionados. Para el nuestro caso se va a mostrar por partes la cosa:

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


