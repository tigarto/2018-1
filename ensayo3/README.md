# ENSAYOS PRELIMINARES - PROCESO DE INSTALACION DE SONATA

> **Objetivos**:
> * Instalar SONATA
> * Documentar la experiencia de instalacion.
> * Hacer los test de chequeo basicos

## 1. Instalacion de SONATA

Para el proceso de instalacion se siguio el siguiente [enlace](https://github.com/sonata-nfv/son-tutorials/blob/master/docs/component_installation.md).

### 1.1. Prerequisitos
Se supone que la maquina en la cual se realizo la instalación de **SONATA** ya cumple con los prerequisitos. Como la maquiba tiene Ubuntu Xenial (16.04) virtualizado por lo cual se siguieron las instrucciones de instalacion para esta distribución.

### 1.2. Instalacion de sonata-cli

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8EC0731023C1F15B
echo "deb http://repo.sonata-nfv.eu ubuntu-xenial main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install sonata-cli
```

Tambien siguiendo el [video de instalacion](https://youtu.be/Hk4j3NcnB4A) para Ubuntu, se ejecutaron los siguientes comandos para verificar la correcta instalacion de la herramienta:

```
son-workspace --help
son-package --help
son-validate --help
son-access --help
son-monitor --help
```

## 2. Instalacion de SONATA's emulation platform

### 2.1. Prerequisitos
A continuacion se muestran los requerimientos que ya se cumplen en la plataforma localmente instalada:
* ansible
* aptitude
* git
* Containernet

### 2.2. Instalacion del emulador

Como los pasos 1 y 2 de la [guia](https://github.com/sonata-nfv/son-tutorials/blob/master/docs/component_installation.md) ya se cumplian solo se llevo a cabo el paso 3, a continuacion se repiten las instrucciones ejecutadas:

```
cd
git clone https://github.com/sonata-nfv/son-emu.git
cd ~/son-emu/ansible
sudo ansible-playbook -i "localhost," -c local install.yml
```



