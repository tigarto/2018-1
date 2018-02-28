#!/usr/bin/python

"""
Simple topology

         c0
          |
          |
   h1 --- s1 --- h3
          |
          |
          h2


Use:

-> Controller: running the pox controller as a switch

   cd $HOME/pox
   ./pox.py log.level --DEBUG forwarding.l2_learning 

-> Topology:

   sudo python simple_topo_containers1.py


References:
- http://csie.nqu.edu.tw/smallko/sdn/lab2.htm
- https://github.com/mininet/mininet/blob/master/examples/controllers.py
"""

from mininet.net import Containernet
from mininet.node import Controller, RemoteController, Docker, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Link

import os

setLogLevel( 'info' )

def networkTest():
    "Create a network with some docker containers acting as hosts."
    net = Containernet(controller=RemoteController)
    info('*** Adding controller\n')
    net.addController('c0')  
    info('*** Creating the network\n')
     # Containers de imagenes con herramientas de red 
    h1 = net.addDocker('h1', ip='10.0.0.100', dimage="ubuntu_net_tools")
    h2 = net.addDocker('h2', ip='10.0.0.101', dimage="ubuntu_net_tools") 
    h3 = net.addDocker('h3', ip='10.0.0.102', dimage="ubuntu_net_tools") 

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')
    

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, h3)
    

    info('*** Build the network\n')
    net.build()
    info('*** Starting network\n')
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network')
    net.stop()

if __name__ == '__main__':
   networkTest()



