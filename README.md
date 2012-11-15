ProxyPublisher
==============

Subscribe to published events from a remote machine.

If you are publishing events with zmq on a remote machine and wants to subscribe on these events from another machine,
then you can use this script as a proxy.

**Use at own risk!**

## How to use it
 - Change the server address
 - Change the subscription key
 - Change the port 
 - Go: python main.py


## Required
 - python
 - zmq binding for python
 - ssh access to remote server


## Trouble shooting
If any problems with pexpect then try http://pypi.python.org/pypi/pexpect-u