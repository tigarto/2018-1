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

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

More info: http://csie.nqu.edu.tw/smallko/sdn/lab2.htm
Use: 

-> Topology and controller:

   ./sudo simple_topo_controller2.py

References:
- https://github.com/mininet/mininet/blob/master/examples/controllers.py
- http://csie.nqu.edu.tw/smallko/sdn/lab2.htm
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topo import SingleSwitchTopo
from mininet.log import setLogLevel, info
from mininet.cli import CLI

import os

setLogLevel( 'info' )

class POXBridge( RemoteController ):
    "Custom Controller class to invoke POX forwarding.l2_learning"

    def __init__(self):        
        Controller.__init__(self, name = 'c0', ip='127.0.0.1', port=6633)
        self.start()
    def start ( self ):
        info('*** "Start POX learning switch \n')
        self.pox = '%s/pox/pox.py' % os.environ[ 'HOME' ]
        self.cmd( self.pox, 'forwarding.l2_learning &' )
        #self.cmd( self.pox, 'forwarding.hub &' )

    def stop ( self ):
         info('*** "Stop POX \n')
         self.cmd( 'kill %' + self.pox )

# controllers = { 'poxbridge': POXBridge }

if __name__ == '__main__':    
    info('*** Create the controller \n')
    c0 = POXBridge()
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


