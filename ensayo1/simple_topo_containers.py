#!/usr/bin/python

"""
This example shows how to create a simple network and
how to create docker containers (based on existing images)
to it.

Two directly connected switches plus a host for each switch:

   h1 --- s1 --- h3
          |
          |
          h2

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

More info: http://mininet.org/walkthrough/
Use: sudo python simple_topo_containers.py 

"""

from mininet.net import Containernet
from mininet.node import Controller, Docker, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Link


def topology():
    "Create a network with some docker containers acting as hosts."

    net = Containernet()    

    info('*** Adding docker containers\n')
    h1 = net.addDocker('h1', ip='10.0.0.100', dimage="ubuntu:latest")
    h2 = net.addDocker('h2', ip='10.0.0.101', dimage="ubuntu:latest") 
    h3 = net.addDocker('h3', ip='10.0.0.102', dimage="ubuntu:latest")  

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')
    

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, h3)
    

    info('*** Starting network\n')
    net.start()
    

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
