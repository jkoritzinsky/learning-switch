import datetime

class Address():
    def __init__(self, addr, port, timestamp):
        self.addr = addr
        self.port = port
        self.timestamp = timestamp

addrs = []

def learnAddr(src, input_port):
    global addrs
    now = datetime.datetime.now()
    addrs = [addr for addr in addrs
        if (now - addr.timestamp).total_seconds() < 10 and addr.addr != src]
    addrs = addrs + [Address(src, input_port, now)]

def getAddr(dest):
    global addrs
    record = next((addr for addr in addrs if addr.addr == dest), None)
    if record != None:
        return record.port
    return None
