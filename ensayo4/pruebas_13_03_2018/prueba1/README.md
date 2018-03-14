# Ejemplo 1

> **Nota**: Este ejemplo es el que se realizo en https://github.com/sonata-nfv/son-emu/wiki/Example-1

## Enunciado
This example shows a very basic use case of the emulator. It does not use any pre-defined service package but shows how a user can manually start two VNF containers and connect (chain) them.

```
+--------+       +--------+
| client <-------> server |
+--------+       +--------+
```

## Pasos

### Preparacion

```
# download test container images used for the examples
docker pull sonatanfv/sonata-empty-vnf
docker pull sonatanfv/sonata-iperf3-vnf
docker pull sonatanfv/sonata-snort-ids-vnf
```

### Instrucciones paso a paso con salida

Se resumen a las mostradas en las siguientes instrucciones:

```
# 1. (Terminal1) start the demo topology
sudo python src/emuvim/examples/sonata_y1_demo_topology_1.py

# 2. (Terminal2) add start two containers in dc2
son-emu-cli compute start -d dc1 -n client -i sonatanfv/sonata-empty-vnf
son-emu-cli compute start -d dc2 -n server -i sonatanfv/sonata-empty-vnf

# 3. (Terminal2) do the chain setup
son-emu-cli network add -b -src client:client-eth0 -dst server:server-eth0

# 4. (Terminal1) check if everything works
containernet> client ping -c2 server

# Output:
PING 10.0.0.4 (10.0.0.4): 56 data bytes
64 bytes from 10.0.0.4: icmp_seq=0 ttl=64 time=0.499 ms
64 bytes from 10.0.0.4: icmp_seq=1 ttl=64 time=0.080 ms
--- 10.0.0.4 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max/stddev = 0.080/0.289/0.499/0.210 ms

# 5. (Terminal1) shutdown the emulator
containernet> exit
```

### Resultados de la aplicacion de las instrucciones
> 1. **Terminal 1**
>```
>
>sudo python sonata_y1_demo_topology_1.py
> ...
>*** Starting controller
>c0 
>*** Starting 3 switches
>dc1.s1 (10ms delay) dc2.s1 (20ms delay) s1 (10ms delay) (20ms delay) ...(10ms delay) (20ms delay) (10ms delay) (20ms delay) 
>*** Starting CLI:
>containernet> nodes
>available nodes are: 
>c0 dc1.s1 dc2.s1 s1
>containernet> net
>dc1.s1 lo:  dc1.s1-eth1:s1-eth1
>dc2.s1 lo:  dc2.s1-eth1:s1-eth2
>s1 lo:  s1-eth1:dc1.s1-eth1 s1-eth2:dc2.s1-eth1
>c0
>containernet> 
>```

> 2. **Terminal 2**
>```
>son-emu-cli compute start -d dc1 -n client -i sonatanfv/sonata-empty-vnf
>{   u'cpu_period': None,
>    u'cpu_quota': -1,
>    u'cpu_shares': None,
>    u'cpuset': None,
>    u'datacenter': u'dc1',
>    u'docker_network': u'172.17.0.2',
>    u'flavor_name': u'tiny',
>    u'hostname': u'client',
>    u'id': u'414f28cc457181bf644d287b1b234d4e80c6fb0991f402c10bdc5aedeea79697',
>    u'image': u'sonatanfv/sonata-empty-vnf',
>    u'mem_limit': None,
>    u'memswap_limit': None,
>    u'name': u'client',
>    u'network': [   {   u'dc_portname': u'dc1.s1-eth2',
>                        u'intf_name': u'client-eth0',
>                        u'ip': u'10.0.0.2/8',
>                        u'mac': u'76:06:79:04:df:b4',
>                        u'netmask': u'8',
>                        u'status': u'OK',
>                        u'up': True,
>                        u'vlan': None}],
>    u'short_id': u'414f28cc4571',
>    u'state': {   u'Dead': False,
>                  u'Error': u'',
>                  u'ExitCode': 0,
>                  u'FinishedAt': u'0001-01-01T00:00:00Z',
>                  u'OOMKilled': False,
>                  u'Paused': False,
>                  u'Pid': 4579,
>                  u'Restarting': False,
>                  u'Running': True,
>                  u'StartedAt': u'2018-03-13T21:06:28.685316492Z',
>                  u'Status': u'running'}}
>
>```
>
>```
>son-emu-cli compute start -d dc2 -n server -i sonatanfv/sonata-empty-vnf
>{   u'cpu_period': None,
>    u'cpu_quota': -1,
>    u'cpu_shares': None,
>    u'cpuset': None,
>    u'datacenter': u'dc2',
>    u'docker_network': u'172.17.0.3',
>    u'flavor_name': u'tiny',
>    u'hostname': u'server',
>    u'id': u'c7d56553338ad379ee25d45a1856d637795937ae55e6df48d8a8836c42913cdc',
>    u'image': u'sonatanfv/sonata-empty-vnf',
>    u'mem_limit': None,
>    u'memswap_limit': None,
>    u'name': u'server',
>    u'network': [   {   u'dc_portname': u'dc2.s1-eth2',
>                        u'intf_name': u'server-eth0',
>                        u'ip': u'10.0.0.4/8',
>                        u'mac': u'66:bc:c9:37:65:60',
>                        u'netmask': u'8',
>                        u'status': u'OK',
>                        u'up': True,
>                        u'vlan': None}],
>    u'short_id': u'c7d56553338a',
>    u'state': {   u'Dead': False,
>                  u'Error': u'',
>                  u'ExitCode': 0,
>                  u'FinishedAt': u'0001-01-01T00:00:00Z',
>                  u'OOMKilled': False,
>                  u'Paused': False,
>                  u'Pid': 4801,
>                  u'Restarting': False,
>                  u'Running': True,
>                  u'StartedAt': u'2018-03-13T21:07:12.96200137Z',
>                  u'Status': u'running'}}
>```
>
>```
> x
>```
