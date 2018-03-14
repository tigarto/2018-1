# Ejemplo 4 ( sonata-snort-service-emu: Service with a single Snort VNF (UPB) Tutorial - Example 3 of the internet web page of sonata-nfv)

> **Nota**: Este ejemplo es tomado de: https://github.com/sonata-nfv/son-emu/wiki/Example-3

## Elementos necesarios
1. Archivo asociado a la topologia: **sonata_y1_demo_topology_1.py**
2. Directorio **sonata-snort-service-emu**

Estos directorios pueden ser descargados de: https://github.com/sonata-nfv/son-examples/tree/master/service-projects


## Enunciado: Example 3 - Snort IDS service package
Deploy Snort IDS service package (from ```son-examples```), manually start additional probing containers (iperf client/server), and connect them to the deployed chain. Check if Snort VNF works correctly and monitors traffic sent between client and server container.

```
+--------+     +-------+     +--------+
| client <-----> snort <-----> server |
+--------+     +-------+     +--------+
```

### Parte 1

Los comandos de manera resumida ejecutados se muestran a continuacion:

```
# 0. package the service-project from the son-examples repository
son-package --project sonata-snort-service-emu -n sonata-snort-service

# 1. (Terminal1) start the demo topology
sudo python sonata_y1_demo_topology_1.py

# 2. (Terminal2) push snort service package to dummy gatekeeper
curl -i -X POST -F package=@sonata-snort-service.son http://127.0.0.1:5000/packages

# 3. (Terminal2) instantiate snort service
curl -X POST http://127.0.0.1:5000/instantiations -d "{}"

# 4. (Terminal2) start additional probing containers (iperf3 client and server)
son-emu-cli compute start -d dc2 -n client -i sonatanfv/sonata-iperf3-vnf
son-emu-cli compute start -d dc2 -n server -i sonatanfv/sonata-iperf3-vnf

# 5. (Terminal2) check if all containers are up
son-emu-cli compute list

# 6. (Terminal2) connect probing containers to chain
son-emu-cli network add -b -src client:client-eth0 -dst snort_vnf:input
son-emu-cli network add -b -src snort_vnf:output -dst server:server-eth0

# 7. (Terminal1) verify that client can connect to server through IDS VNF
containernet>  client ping -c20 server

# 8. (Terminal1) verify that the Snort IDS investigated our ping traffic
containernet> snort_vnf cat /snort-logs/10.0.0.8/ICMP_ECHO_REPLY

# 9. (Terminal1) Start iperf3 server in server container
containernet> server iperf3 -s &

# 10. (Terminal1) Start iperf3 client and send TCP traffic for 10 seconds
containernet> client iperf3 -c 10.0.0.8 -t 10
```

### Parte 2

Los comandos de manera resumida ejecutados se muestran a continuacion:

```
# 9. (Terminal1) Start iperf3 server in server container
containernet> server iperf3 -s &

# 10. (Terminal1) Start iperf3 client and send TCP traffic for 10 seconds
containernet> client iperf3 -c 10.0.0.8 -t 10
```

### Parte 3

Los comandos de manera resumida ejecutados se muestran a continuacion:

```
# (Terminal 3) Attach to VNF container to monitor alerts
docker exec -it mn.snort_vnf /bin/bash
tail -f /snort-logs/alert

# (Terminal 1) Try a normal SSH connection on port 22
client ssh server

# (Terminal 3) Output:
[**] [1:9999998:1] Attention! Some bad guy wants to SSH into your network (tcp:22)! [**] [Priority: 0] {TCP} 10.0.0.6:37990 -> 10.0.0.8:22

# (Terminal 1) Lets try SSH on another port
server ncat -k -l 12345 & 
client ssh -o ConnectTimeout=1 -p 12345 server

# (Terminal 3) No output! We don't detect it. Lets add a rule to our Snort config to do DPI-based detection
vim /etc/snort/snort.conf
# uncomment last line:
alert tcp any any -> any any (msg:"Attention! Some bad guy wants to SSH into your network!";content:"SSH-";sid:9999999;rev:1)
# save, restart snort and start monitoring again
sh restart_snort.sh 
tail -f /snort-logs/alert

# (Terminal 1) Lets try SSH on another port again
client ssh -o ConnectTimeout=1 -p 12345 server

# (Terminal 3) Now we detect SSH connections an any port:
[**] [1:9999999:1] Attention! Some bad guy wants to SSH into your network! [**] [Priority: 0] {TCP} 10.0.0.6:60131 -> 10.0.0.8:12345
```

**Nota**: El comando **0. package the service-project from the son-examples repository** se modifico, pues en la [guia](https://github.com/sonata-nfv/son-emu/wiki/Example-2) el que aparece, no es.

### Resultados de la aplicacion de las instrucciones

**Terminal1**

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
curl -i -X POST -F package=@sonata-snort-service.son http://127.0.0.1:5000/packages
HTTP/1.1 100 Continue

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 159
Server: Werkzeug/0.14.1 Python/2.7.12
Date: Tue, 13 Mar 2018 22:45:39 GMT



{
    "error": null, 
    "service_uuid": "8380ea95-1dea-4550-94c3-7c077c1a6770", 
    "sha1": "11162f9bb17847936f49d5a5f6295afcf137bfe4", 
    "size": 3601
}
```

```
curl -X POST http://127.0.0.1:5000/instantiations -d "{}"
{
    "service_instance_uuid": "43d0664d-a06a-4113-83f2-f4b0cb447c48"
}
```

```
son-emu-cli compute start -d dc2 -n client -i sonatanfv/sonata-iperf3-vnf
{   u'cpu_period': None,
    u'cpu_quota': -1,
    u'cpu_shares': None,
    u'cpuset': None,
    u'datacenter': u'dc2',
    u'docker_network': u'172.17.0.3',
    u'flavor_name': u'tiny',
    u'hostname': u'client',
    u'id': u'5c1ddd45e040319ea28b3cb36ee5ac3827ee6c639f5fbbe507968ef85e146dc1',
    u'image': u'sonatanfv/sonata-iperf3-vnf',
    u'mem_limit': None,
    u'memswap_limit': None,
    u'name': u'client',
    u'network': [   {   u'dc_portname': u'dc2.s1-eth5',
                        u'intf_name': u'client-eth0',
                        u'ip': u'10.0.0.6/8',
                        u'mac': u'02:ec:78:95:21:12',
                        u'netmask': u'8',
                        u'status': u'OK',
                        u'up': True,
                        u'vlan': None}],
    u'short_id': u'5c1ddd45e040',
    u'state': {   u'Dead': False,
                  u'Error': u'',
                  u'ExitCode': 0,
                  u'FinishedAt': u'0001-01-01T00:00:00Z',
                  u'OOMKilled': False,
                  u'Paused': False,
                  u'Pid': 11394,
                  u'Restarting': False,
                  u'Running': True,
                  u'StartedAt': u'2018-03-13T22:46:45.664387516Z',
                  u'Status': u'running'}}
```


```
son-emu-cli compute start -d dc2 -n server -i sonatanfv/sonata-iperf3-vnf
{   u'cpu_period': None,
    u'cpu_quota': -1,
    u'cpu_shares': None,
    u'cpuset': None,
    u'datacenter': u'dc2',
    u'docker_network': u'172.17.0.4',
    u'flavor_name': u'tiny',
    u'hostname': u'server',
    u'id': u'34e53f4cbca328d8c8988971fb7f5b86e136347e96a0aa7987db6061f1a888e8',
    u'image': u'sonatanfv/sonata-iperf3-vnf',
    u'mem_limit': None,
    u'memswap_limit': None,
    u'name': u'server',
    u'network': [   {   u'dc_portname': u'dc2.s1-eth6',
                        u'intf_name': u'server-eth0',
                        u'ip': u'10.0.0.8/8',
                        u'mac': u'02:ef:c1:9c:f7:10',
                        u'netmask': u'8',
                        u'status': u'OK',
                        u'up': True,
                        u'vlan': None}],
    u'short_id': u'34e53f4cbca3',
    u'state': {   u'Dead': False,
                  u'Error': u'',
                  u'ExitCode': 0,
                  u'FinishedAt': u'0001-01-01T00:00:00Z',
                  u'OOMKilled': False,
                  u'Paused': False,
                  u'Pid': 11594,
                  u'Restarting': False,
                  u'Running': True,
                  u'StartedAt': u'2018-03-13T22:47:46.590836939Z',
                  u'Status': u'running'}}
```
```
son-emu-cli compute list
+--------------+-------------+--------------------------------+-------------------+-------------------------------------+
| Datacenter   | Container   | Image                          | Interface list    | Datacenter interfaces               |
+==============+=============+================================+===================+=====================================+
| dc2          | snort_vnf   | sonatanfv/sonata-snort-ids-vnf | mgmt,input,output | dc2.s1-eth2,dc2.s1-eth3,dc2.s1-eth4 |
+--------------+-------------+--------------------------------+-------------------+-------------------------------------+
| dc2          | client      | sonatanfv/sonata-iperf3-vnf    | client-eth0       | dc2.s1-eth5                         |
+--------------+-------------+--------------------------------+-------------------+-------------------------------------+
| dc2          | server      | sonatanfv/sonata-iperf3-vnf    | server-eth0       | dc2.s1-eth6                         |
+--------------+-------------+--------------------------------+-------------------+-------------------------------------+
```


```
son-emu-cli network add -b -src client:client-eth0 -dst snort_vnf:input
"success: add-flow between client and snort_vnf with options: {
 "priority": "1000", 
 "path": [
  "dc2.s1"
 ], 
 "vlan": 2, 
 "cookie": "10", 
 "match_input": null
}
success: add-flow between snort_vnf and client with options: {
 "priority": "1000", 
 "path": [
  "dc2.s1"
 ], 
 "vlan": 3, 
 "cookie": "10", 
 "match_input": null
}"
```

```
son-emu-cli network add -b -src snort_vnf:output -dst server:server-eth0
"success: add-flow between snort_vnf and server with options: {
 "priority": "1000", 
 "path": [
  "dc2.s1"
 ], 
 "vlan": 4, 
 "cookie": "10", 
 "match_input": null
}
success: add-flow between server and snort_vnf with options: {
 "priority": "1000", 
 "path": [
  "dc2.s1"
 ], 
 "vlan": 5, 
 "cookie": "10", 
 "match_input": null
}"
```

**Terminal 1**

```
containernet> client ping -c20 server
PING 10.0.0.8 (10.0.0.8): 56 data bytes
64 bytes from 10.0.0.8: icmp_seq=0 ttl=64 time=0.980 ms
64 bytes from 10.0.0.8: icmp_seq=1 ttl=64 time=0.109 ms
64 bytes from 10.0.0.8: icmp_seq=2 ttl=64 time=0.242 ms
64 bytes from 10.0.0.8: icmp_seq=3 ttl=64 time=0.121 ms
64 bytes from 10.0.0.8: icmp_seq=4 ttl=64 time=0.089 ms
64 bytes from 10.0.0.8: icmp_seq=5 ttl=64 time=0.175 ms
64 bytes from 10.0.0.8: icmp_seq=6 ttl=64 time=0.087 ms
64 bytes from 10.0.0.8: icmp_seq=7 ttl=64 time=0.079 ms
64 bytes from 10.0.0.8: icmp_seq=8 ttl=64 time=0.167 ms
64 bytes from 10.0.0.8: icmp_seq=9 ttl=64 time=0.195 ms
64 bytes from 10.0.0.8: icmp_seq=10 ttl=64 time=0.189 ms
64 bytes from 10.0.0.8: icmp_seq=11 ttl=64 time=0.189 ms
64 bytes from 10.0.0.8: icmp_seq=12 ttl=64 time=0.113 ms
64 bytes from 10.0.0.8: icmp_seq=13 ttl=64 time=0.088 ms
64 bytes from 10.0.0.8: icmp_seq=14 ttl=64 time=0.099 ms
64 bytes from 10.0.0.8: icmp_seq=15 ttl=64 time=0.104 ms
64 bytes from 10.0.0.8: icmp_seq=16 ttl=64 time=0.086 ms
64 bytes from 10.0.0.8: icmp_seq=17 ttl=64 time=0.091 ms
64 bytes from 10.0.0.8: icmp_seq=18 ttl=64 time=0.099 ms
64 bytes from 10.0.0.8: icmp_seq=19 ttl=64 time=0.085 ms
--- 10.0.0.8 ping statistics ---
20 packets transmitted, 20 packets received, 0% packet loss
round-trip min/avg/max/stddev = 0.079/0.169/0.980/0.192 ms          
```

```
containernet> snort_vnf cat /snort-logs/10.0.0.8/ICMP_ECHO_REPLY
[**] Ping! [**]
03/13-22:49:37.218209 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32299 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:0  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:38.218995 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32338 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:1  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:39.220518 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32371 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:2  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:40.221658 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32515 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:3  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:41.224282 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32607 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:4  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:42.225540 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32717 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:5  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:43.226517 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32854 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:6  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:44.228013 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:32878 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:7  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:45.229355 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:33076 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:8  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:46.230755 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:33203 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:9  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:47.232082 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:33301 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:10  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:48.237811 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:33540 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:11  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:49.238685 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:33726 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:12  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:50.238836 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:33952 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:13  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:51.239926 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:34193 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:14  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:52.241545 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:34205 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:15  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:53.242740 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:34288 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:16  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:54.244306 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:34409 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:17  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:55.244573 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:34529 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:18  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

[**] Ping! [**]
03/13-22:49:56.246004 10.0.0.8 -> 10.0.0.6
ICMP TTL:64 TOS:0x0 ID:34758 IpLen:20 DgmLen:84
Type:0  Code:0  ID:26  Seq:19  ECHO REPLY
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
```

### Parte 2

**Terminal 1**

```
containernet> server iperf3 -s &
```

```
containernet> client iperf3 -c 10.0.0.8 -t 10
Connecting to host 10.0.0.8, port 5201
[  4] local 10.0.0.6 port 35576 connected to 10.0.0.8 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec  1.26 GBytes  10.8 Gbits/sec  669    973 KBytes       
[  4]   1.00-2.00   sec  1.08 GBytes  9.28 Gbits/sec    0   1.04 MBytes       
[  4]   2.00-3.00   sec   900 MBytes  7.58 Gbits/sec    0   1.19 MBytes       
[  4]   3.00-4.00   sec  1.07 GBytes  9.22 Gbits/sec    0   1.23 MBytes       
[  4]   4.00-5.00   sec  1.11 GBytes  9.52 Gbits/sec    0   1.27 MBytes       
[  4]   5.00-6.00   sec   974 MBytes  8.17 Gbits/sec    0   1.30 MBytes       
[  4]   6.00-7.00   sec   979 MBytes  8.20 Gbits/sec    0   1.32 MBytes       
[  4]   7.00-8.00   sec  1011 MBytes  8.49 Gbits/sec    0   1.36 MBytes       
[  4]   8.00-9.00   sec  1.25 GBytes  10.7 Gbits/sec  863   1.02 MBytes       
[  4]   9.00-10.00  sec   919 MBytes  7.71 Gbits/sec    0   1.19 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  10.5 GBytes  8.98 Gbits/sec  1532             sender
[  4]   0.00-10.00  sec  10.4 GBytes  8.96 Gbits/sec                  receiver

iperf Done.
```

```
containernet> snort_vnf ls /snort-logs/10.0.0.6
ICMP_ECHO  TCP:35574-5201  TCP:35576-5201
```

### Parte 3

**Terminal 3**
```
sudo docker exec -it mn.snort_vnf /bin/bash
[sudo] password for osboxes: 
root@snort_vnf:/# 
```

```
root@snort_vnf:/# tail -f /snort-logs/alert
```

**Terminal 1**
```
containernet> client ssh server
ssh: connect to host 10.0.0.8 port 22: Connection refused
```

Cuando se ejecuta el comando anterior la salida en la terminal 3 es la siguiente:


**Terminal 3**
```
root@snort_vnf:/# tail -f /snort-logs/alert
03/13-22:55:03.956003  [**] [1:9999998:1] Attention! Some bad guy wants to SSH into your network (tcp:22)! [**] [Priority: 0] {TCP} 10.0.0.6:48214 -> 10.0.0.8:22
```

**ACA VAMOS...**
