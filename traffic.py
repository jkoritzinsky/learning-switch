from switchyard.lib.userlib import log_debug

addrs = []

class Address():
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.traffic = 0
    
    def add_traffic(self):
        self.traffic = self.traffic + 1

    def __repr__(self):
        return "{} on port {}. Traffic: {}".format(self.addr, self.port, self.traffic)

def learnAddr(src, input_port):
    global addrs
    record = next((addr for addr in addrs if addr.addr == src), None)
    if record != None:
        record.port = input_port
    else:
        addrs.sort(key=lambda x: -x.traffic)
        addrs = addrs[:4]
        addrs.append(Address(src, input_port))
    log_debug("Learned: {}".format(addrs))

def getAddr(dest):
    global addrs
    record = next((addr for addr in addrs if addr.addr == dest), None)
    if record != None:
        record.add_traffic()
        return record.port
    return None
