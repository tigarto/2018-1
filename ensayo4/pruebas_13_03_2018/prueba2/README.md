# Ejemplo 2

> **Nota**: Este ejemplo es el que se realizo en https://github.com/sonata-nfv/son-emu

## Enunciado
This simple example shows how to start the emulator with a simple topology (terminal 1) and how to start (terminal 2) some empty VNF containers in the emulated datacenters (PoPs) by using the son-emu-cli.

## Pasos

### Preparacion

Previo al trabajo esta simulacion (y hasta con las otras), fue necesario tener certeza y asegurarnos que la version de docker fuera la 2.0.2. En nuestra maquina al momento se tuvo problemas con la version, por lo que fue necesario mientras se intentaba correr el ejemplo, reinstalar con el pip esta version del docker tal y como se muestra a continuacion:

```
sudo pip install docker==2.0.2
```

Se coloca en este caso como preparacion para evitar tener el problema que en su momento se tuvo cuando se intento simular.

### Instrucciones paso a paso con salida

Se resumen a las mostradas en las siguientes instrucciones:

**First terminal (start the emulation platform)**:

```
sudo python src/emuvim/examples/simple_topology.py
```

**Second terminal**:

```
son-emu-cli compute start -d datacenter1 -n vnf1
son-emu-cli compute start -d datacenter1 -n vnf2
son-emu-cli compute list
```

**First terminal**:
```
containernet> vnf1 ifconfig
containernet> vnf1 ping -c 2 vnf2
```

### Resultados de la aplicacion de las instrucciones

**First terminal (start the emulation platform)**:

```
sudo python simple_topology.py
...
*** Starting CLI:
containernet> 
```

**Second terminal**:

```
sudo son-emu-cli compute start -d datacenter1 -n vnf1
{   u'cpu_period': None,
    u'cpu_quota': -1,
    u'cpu_shares': None,
    u'cpuset': None,
    u'datacenter': u'datacenter1',
    u'docker_network': u'172.17.0.2',
    u'flavor_name': u'tiny',
    u'hostname': u'vnf1',
    u'id': u'd9bbb4f4835fe6f4b4b70685cabf35f39b90871c6d8610abe60e9ce46b124763',
    u'image': u'ubuntu:trusty',
    u'mem_limit': None,
    u'memswap_limit': None,
    u'name': u'vnf1',
    u'network': [   {   u'dc_portname': u'dc1.s1-eth3',
                        u'intf_name': u'vnf1-eth0',
                        u'ip': u'10.0.0.2/8',
                        u'mac': u'46:0f:71:d1:eb:a5',
                        u'netmask': u'8',
                        u'status': u'OK',
                        u'up': True,
                        u'vlan': None}],
    u'short_id': u'd9bbb4f4835f',
    u'state': {   u'Dead': False,
                  u'Error': u'',
                  u'ExitCode': 0,
                  u'FinishedAt': u'0001-01-01T00:00:00Z',
                  u'OOMKilled': False,
                  u'Paused': False,
                  u'Pid': 9508,
                  u'Restarting': False,
                  u'Running': True,
                  u'StartedAt': u'2018-03-13T22:27:47.653391942Z',
                  u'Status': u'running'}}


son-emu-cli compute start -d datacenter1 -n vnf2
{   u'cpu_period': None,
    u'cpu_quota': -1,
    u'cpu_shares': None,
    u'cpuset': None,
    u'datacenter': u'datacenter1',
    u'docker_network': u'172.17.0.3',
    u'flavor_name': u'tiny',
    u'hostname': u'vnf2',
    u'id': u'58187e843bb833fcbcc9c1760aee57ac5424c48c247f98f4cd54a2d234e37c12',
    u'image': u'ubuntu:trusty',
    u'mem_limit': None,
    u'memswap_limit': None,
    u'name': u'vnf2',
    u'network': [   {   u'dc_portname': u'dc1.s1-eth4',
                        u'intf_name': u'vnf2-eth0',
                        u'ip': u'10.0.0.4/8',
                        u'mac': u'd6:ad:92:f9:d8:f9',
                        u'netmask': u'8',
                        u'status': u'OK',
                        u'up': True,
                        u'vlan': None}],
    u'short_id': u'58187e843bb8',
    u'state': {   u'Dead': False,
                  u'Error': u'',
                  u'ExitCode': 0,
                  u'FinishedAt': u'0001-01-01T00:00:00Z',
                  u'OOMKilled': False,
                  u'Paused': False,
                  u'Pid': 9732,
                  u'Restarting': False,
                  u'Running': True,
                  u'StartedAt': u'2018-03-13T22:28:40.837419413Z',
                  u'Status': u'running'}}
                  
son-emu-cli compute list
+--------------+-------------+---------------+------------------+-------------------------+
| Datacenter   | Container   | Image         | Interface list   | Datacenter interfaces   |
+==============+=============+===============+==================+=========================+
| datacenter1  | vnf2        | ubuntu:trusty | vnf2-eth0        | dc1.s1-eth4             |
+--------------+-------------+---------------+------------------+-------------------------+
| datacenter1  | vnf1        | ubuntu:trusty | vnf1-eth0        | dc1.s1-eth3             |
+--------------+-------------+---------------+------------------+-------------------------+
```
**First terminal**:

```
containernet> vnf1 ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:ac:11:00:02  
          inet addr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:29 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:4152 (4.1 KB)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

vnf1-eth0 Link encap:Ethernet  HWaddr 46:0f:71:d1:eb:a5  
          inet addr:10.0.0.2  Bcast:10.255.255.255  Mask:255.0.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:33 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:4884 (4.8 KB)  TX bytes:0 (0.0 B)


containernet> vnf1 ping -c 2 vnf2
PING 10.0.0.4 (10.0.0.4) 56(84) bytes of data.
64 bytes from 10.0.0.4: icmp_seq=1 ttl=64 time=7.55 ms
64 bytes from 10.0.0.4: icmp_seq=2 ttl=64 time=0.054 ms

--- 10.0.0.4 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 0.054/3.805/7.556/3.751 ms

containernet> exit
```

