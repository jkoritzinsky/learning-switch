'''
Ethernet learning swith with pluggable learning algorithm
'''
from switchyard.lib.userlib import *

def main(net, learner):
    my_interfaces = net.interfaces() 
    mymacs = [intf.ethaddr for intf in my_interfaces]

    while True:
        try:
            timestamp,input_port,packet = net.recv_packet()
        except NoPackets:
            continue
        except Shutdown:
            return
        
        learner.learnAddr(packet[0].src, input_port)

        log_debug ("In {} received packet {} on {}".format(net.name, packet, input_port))
        if packet[0].dst in mymacs:
            log_debug ("Packet intended for me")
        else:
            output_port = learner.getAddr(packet[0].dst)
            if output_port == None:
                for intf in my_interfaces:
                    if input_port != intf.name:
                        log_debug ("Flooding packet {} to {}".format(packet, intf.name))
                        net.send_packet(intf.name, packet)
            else:
                net.send_packet(output_port, packet)
    net.shutdown()
