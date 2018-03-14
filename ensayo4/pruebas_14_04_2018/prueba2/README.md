# Ejemplo 3 (Example 2 of de internet web page of sonata-nfv)

> **Nota**: Este ejemplo es tomado de: https://github.com/sonata-nfv/son-emu/wiki/Example-2

## Elementos necesarios
1. Archivo asociado a la topologia: **sonata_y1_demo_topology_1.py**
2. Directorio **sonata-snort-service-emu**
3. Directorio **sonata-empty-service-emu**

Estos directorios pueden ser descargados de: https://github.com/sonata-nfv/son-examples/tree/master/service-projects

**Comentario**: 
* No se para que, pero al parecer el directorio **sonata-snort-service-emu** no era necesario.

## Enunciado: Example 2 - Empty demo service package
Deploy SONATA empty service package (from ```son-examples```) and check if the containers are deployed correctly and the automatic chaining setup works.

```
+--------+     +-------+     +--------+
|  vnf1  <-----> vnf2  <----->  vnf3  |
+--------+     +-------+     +--------+
```

Los comandos de manera resumida ejecutados se muestran a continuacion:

```
# 0. package the service-project from the son-examples repository
son-package --project sonata-empty-service-emu -n sonata-empty-service-emu

# 1. (Terminal1) start the demo topology
sudo python src/emuvim/examples/sonata_y1_demo_topology_1.py

# 2. (Terminal2) push empty service package to dummy gatekeeper
curl -i -X POST -F package=@sonata-empty-service.son http://127.0.0.1:5000/packages

# 3. (Terminal2) instantiate snort service
curl -X POST http://127.0.0.1:5000/instantiations -d "{}"

# 4. (Terminal2) check if all containers are up
son-emu-cli compute list

# 5. (Terminal1) lets check the network config of one container
containernet>  empty_vnf2 ifconfig

# 6. (Terminal1) verify that the chained connection between vnf1 and vnf2 works
containernet> empty_vnf1 ping -c 2 200.0.0.2

# 7. (Terminal1) verify that the chained connection between vnf2 and vnf3 works
containernet> empty_vnf2 ping -c 2 201.0.0.2

# 8. (Terminal1) shutdown the emulator
containernet> exit
```

**Nota**: El comando **0. package the service-project from the son-examples repository** se modifico, pues en la [guia](https://github.com/sonata-nfv/son-emu/wiki/Example-2) el que aparece, no es.

### Resultados de la aplicacion de las instrucciones

**Terminal1**

```
son-package --project sonata-empty-service-emu -n sonata-empty-service
son-package --project sonata-empty-service-emu -n sonata-empty-service
2018-03-14 11:17:54 osboxes son.workspace.project[25050] INFO Loading Project configuration 'sonata-empty-service-emu/project.yml'
2018-03-14 11:17:54 osboxes requests.packages.urllib3.connectionpool[25050] INFO Starting new HTTP connection (1): sp.int3.sonata-nfv.eu
2018-03-14 11:17:54 osboxes son.package.package[25050] INFO Create Package Content Section
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating service 'sonata-empty-service-emu/sources/nsd/nsd.yml'
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO ... syntax: True, integrity: False, topology: False
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating syntax of service 'eu.sonata-nfv.sonata-empty-service.0.1'
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO Packaging VNF descriptors from project source...
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating function 'sonata-empty-service-emu/sources/vnf/empty-vnf1/empty-vnf1-vnfd.yml'
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO ... syntax: True, integrity: False, topology: False
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating syntax of function 'eu.sonata-nfv.empty-vnf1.0.1'
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating function 'sonata-empty-service-emu/sources/vnf/empty-vnf3/empty-vnf3-vnfd.yml'
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO ... syntax: True, integrity: False, topology: False
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating syntax of function 'eu.sonata-nfv.empty-vnf3.0.1'
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating function 'sonata-empty-service-emu/sources/vnf/empty-vnf2/empty-vnf2-vnfd.yml'
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO ... syntax: True, integrity: False, topology: False
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating syntax of function 'eu.sonata-nfv.empty-vnf2.0.1'
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO package_pcs executed in 0.472 sec
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO Create Package Resolver Section
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO package_prs executed in 0.000 sec
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO Create Package Dependencies Section
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO package_pds executed in 0.000 sec
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO Create Artifact Dependencies Section
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO package_ads executed in 0.000 sec
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO Create General Description section
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO package_gds executed in 0.000 sec
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating package '/home/osboxes/Documents/2018-1/ensayo4/pruebas_14_04_2018/prueba1/sonata-empty-service.son'
2018-03-14 11:17:55 osboxes son.validate.validate[25050] INFO Validating syntax of package descriptor 'eu.sonata-nfv.package.sonata-empty-service.0.4'
2018-03-14 11:17:55 osboxes son.package.package[25050] INFO Package generated successfully.
File: /home/osboxes/Documents/2018-1/ensayo4/pruebas_14_04_2018/prueba1/sonata-empty-service.son
MD5: 56dcf6a3dab23f861791d770d1cc151f
```

```
sudo python sonata_y1_demo_topology_1.py
...
*** Starting controller
c0 
*** Starting 3 switches
dc1.s1 (10ms delay) dc2.s1 (20ms delay) s1 (10ms delay) (20ms delay) ...(10ms delay) (20ms delay) (10ms delay) (20ms delay) 
*** Starting CLI:
containernet> 
```

**Terminal2**
```
curl -i -X POST -F package=@sonata-empty-service.son http://127.0.0.1:5000/packages
HTTP/1.1 100 Continue

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 159
Server: Werkzeug/0.14.1 Python/2.7.12
Date: Wed, 14 Mar 2018 15:18:46 GMT

{
    "error": null, 
    "service_uuid": "dd2da66c-f06f-4f11-8058-a354eb41b872", 
    "sha1": "1372e8d442abfb2caca2a1ab71c4f1fef8b2ecdd", 
    "size": 7098
}
```

```
son-emu-cli compute list
+--------------+-------------+---------+------------------+-------------------------+
| Datacenter   | Container   | Image   | Interface list   | Datacenter interfaces   |
+==============+=============+=========+==================+=========================+
+--------------+-------------+---------+------------------+-------------------------+
```

```
curl -X POST http://127.0.0.1:5000/instantiations -d "{}"
{
    "service_instance_uuid": "a1a81812-836b-4b5d-9dbc-e8a93995bbff"
}
```

```
son-emu-cli compute list
+--------------+-------------+----------------------------+-------------------+-------------------------------------+
| Datacenter   | Container   | Image                      | Interface list    | Datacenter interfaces               |
+==============+=============+============================+===================+=====================================+
| dc2          | empty_vnf2  | sonatanfv/sonata-empty-vnf | mgmt,input,output | dc2.s1-eth2,dc2.s1-eth3,dc2.s1-eth4 |
+--------------+-------------+----------------------------+-------------------+-------------------------------------+
| dc2          | empty_vnf1  | sonatanfv/sonata-empty-vnf | mgmt,input,output | dc2.s1-eth5,dc2.s1-eth6,dc2.s1-eth7 |
+--------------+-------------+----------------------------+-------------------+-------------------------------------+
| dc1          | empty_vnf3  | sonatanfv/sonata-empty-vnf | mgmt,input,output | dc1.s1-eth2,dc1.s1-eth3,dc1.s1-eth4 |
+--------------+-------------+----------------------------+-------------------+-------------------------------------+
```

**Terminal 1**

```
containernet> empty_vnf2 ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:02  
          inet addr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:58 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:8606 (8.6 KB)  TX bytes:0 (0.0 B)

input     Link encap:Ethernet  HWaddr 76:8e:c1:7e:43:23  
          inet addr:10.30.0.2  Bcast:10.30.0.3  Mask:255.255.255.252
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:29 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:4205 (4.2 KB)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

mgmt      Link encap:Ethernet  HWaddr 02:c1:43:68:da:33  
          inet addr:10.20.0.2  Bcast:10.20.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:25 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3659 (3.6 KB)  TX bytes:0 (0.0 B)

output    Link encap:Ethernet  HWaddr b6:31:4e:ff:a7:74  
          inet addr:10.30.1.1  Bcast:10.30.1.3  Mask:255.255.255.252
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:25 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3659 (3.6 KB)  TX bytes:0 (0.0 B
          
```

```
containernet> empty_vnf1 ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:04  
          inet addr:172.17.0.4  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:51 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:6811 (6.8 KB)  TX bytes:692 (692.0 B)

input     Link encap:Ethernet  HWaddr 2e:52:81:a5:62:77  
          inet addr:10.0.0.11  Bcast:10.255.255.255  Mask:255.0.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:37 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:4730 (4.7 KB)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:4 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:448 (448.0 B)  TX bytes:448 (448.0 B)

mgmt      Link encap:Ethernet  HWaddr 82:92:97:3d:21:0d  
          inet addr:10.20.0.1  Bcast:10.20.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:28 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:4002 (4.0 KB)  TX bytes:0 (0.0 B)

output    Link encap:Ethernet  HWaddr 12:cd:22:d2:f2:15  
          inet addr:10.30.0.1  Bcast:10.30.0.3  Mask:255.255.255.252
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:27 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3932 (3.9 KB)  TX bytes:252 (252.0 B)

```

```
containernet> empty_vnf1 ping -c 2 10.30.0.2
PING 10.30.0.2 (10.30.0.2): 56 data bytes
92 bytes from 10.30.0.1: Destination Host Unreachable
92 bytes from 10.30.0.1: Destination Host Unreachable
--- 10.30.0.2 ping statistics ---
2 packets transmitted, 0 packets received, 100% packet loss
```

A diferencia de lo que se muestra en el tutorial las direcciones IP cambian, por otro lado, este ping no da.

```
containernet> empty_vnf2 ping -c 2 10.30.1.2
PING 10.30.1.2 (10.30.1.2): 56 data bytes
64 bytes from 10.30.1.2: icmp_seq=0 ttl=64 time=134.546 ms
64 bytes from 10.30.1.2: icmp_seq=1 ttl=64 time=62.297 ms
--- 10.30.1.2 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max/stddev = 62.297/98.421/134.546/36.125 ms
```

```
containernet> exit
*** Stopping 1 controllers
c0 
*** Stopping 11 links
...........
*** Stopping 3 switches
dc1.s1 dc2.s1 s1 
*** Stopping 3 hosts
empty_vnf2 empty_vnf3 empty_vnf1 
*** Done
*** Removing NAT rules of 0 SAPs

Unhandled exception in thread started by <bound method Thread.__bootstrap of <Thread(Thread-2, stopped daemon 140231391500032)>>
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 774, in __bootstrap
    self.__bootstrap_inner()
  File "/usr/lib/python2.7/threading.py", line 814, in __bootstrap_inner
    (self.name, _format_exc()))
  File "/usr/lib/python2.7/traceback.py", line 241, in format_exc
    etype, value, tb = sys.exc_info()
AttributeError: 'NoneType' object has no attribute 'exc_info'
```

La salida del comando anterior vemos que da un error todo raro.
