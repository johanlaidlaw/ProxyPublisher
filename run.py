'''
Created by Johan Laidlaw
Date: 2012-11-15
'''


import json
import zmq
from zmq import ssh

def main():
    # Prepare our context and publisher
    context    = zmq.Context(1)
    subscriber = context.socket(zmq.SUB)
    ssh.tunnel_connection(subscriber, "tcp://127.0.0.1:6273", "username@myserver.com")
    subscriber.setsockopt(zmq.SUBSCRIBE, "key")
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:6273")

    while True:
        # Read envelope with address
        [address, contents] = subscriber.recv_multipart()
        print("[%s] %s\n" % (address, contents))

        publisher.send_multipart([address,contents])
    
    # We never get here but clean up anyhow
    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()