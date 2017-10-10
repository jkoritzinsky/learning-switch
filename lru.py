import datetime

    def __init__(self, addr, port, timestamp):
        self.addr = addr
        self.port = port
        self.timestamp = timestamp

    def __repr__(self):
        return "{} on port {}. Traffic: {}".format(self.addr, self.port, self.traffic)

addrs = []

def learnAddr(src, input_port):
    global addrs
    record = next((addr for addr in addrs if addr.addr == src), None)
    if record != None:
        record.port = input_port
    else:
        addrs.sort(key=lambda x: -x.timestamp)
        addrs = addrs[:4]
        addrs.append(Address(src, input_port))
    log_debug("Learned: {}".format(addrs))

def getAddr(dest):
    global addrs
    record = next((addr for addr in addrs if addr.addr == dest), None)
    if record != None:
        return record.port
    return None
