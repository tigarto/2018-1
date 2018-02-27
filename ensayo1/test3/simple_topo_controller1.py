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

   ./sudo simple_topo_controller1.py


References:
- http://csie.nqu.edu.tw/smallko/sdn/lab2.htm
- https://github.com/mininet/mininet/blob/master/examples/controllers.py
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topo import SingleSwitchTopo
from mininet.log import setLogLevel, info
from mininet.cli import CLI

import os

setLogLevel( 'info' )

if __name__ == '__main__':    
    info('*** Create the controller \n')
    c0 = RemoteController('c0')
    info('*** Creating the network\n')
    net = Mininet(topo=SingleSwitchTopo(3), build=False)
    info('*** Adding the controller to network the network\n')
    net.addController(c0)
    info('*** Build the network\n')
    net.build()
    info('*** Starting network\n')
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network')
    net.stop()


