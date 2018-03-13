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



