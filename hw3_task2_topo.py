
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import Controller, RemoteController, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf

def aggNet():
        controller_ip = "127.0.0.1"
        net = Mininet(topo=None,build=False, link=TCLink)
        c1 = net.addController(name = 'c0', controller=RemoteController, ip=controller_ip)
        h1 = net.addHost('h1')
        h2 = net.addHost('h2')
        h3 = net.addHost('h3')
        h4 = net.addHost('h4')
        h5 = net.addHost('h5')
        s1 = net.addSwitch('s1')
        s2 = net.addSwitch('s2')
        s3 = net.addSwitch('s3')

        net.addLink(h1,s1, delay='2000ms')
        net.addLink(h2,s1, delay='2000ms')

        net.addLink(h3,s2, delay='2000ms')

        net.addLink(h4,s3, delay='2000ms')
        net.addLink(h5,s3, delay='2000ms')

        net.addLink(s1,s2, delay='2000ms')
        net.addLink(s2,s3, delay='2000ms')


        net.start()
        
        h1.cmd('dhclient -r h1-eth0')
        h1.cmd('dhclient -4 h1-eth0')
        h2.cmd('dhclient -r h2-eth0')
        h2.cmd('dhclient -4 h2-eth0')
        h3.cmd('dhclient -r h3-eth0')
        h3.cmd('dhclient -4 h3-eth0')
        h4.cmd('dhclient -r h4-eth0')
        h4.cmd('dhclient -4 h4-eth0')
        h5.cmd('dhclient -r h5-eth0')
        h5.cmd('dhclient -4 h5-eth0')
        

        CLI( net )
        net.stop()

if __name__ == '__main__':
        setLogLevel( 'info' )
        aggNet()
