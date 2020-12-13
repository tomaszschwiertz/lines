#!/usr/bin/env python3
import requests
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

url="https://raw.githubusercontent.com/tomaszschwiertz/lines/master/prefix"
read_data = requests.get(url).content.decode('utf8')

list = read_data.split()
set_cmd = """
"""

for x in range (0, len(list)):
    set_cmd += ("set policy-options prefix-list PXL-CUSTOMERS " + list[x] + "\n")

U="netconfuser"
P="netconf123"
ROUTERS = ["192.0.2.1", "192.0.2.2", "192.0.2.3"]

for device in ROUTERS:
    dev = Device(device, port=830, user=U, password=P)
    dev.open()
    conf = Config(dev)
    conf.lock()
    conf.load(set_cmd, format='set')
    print('Updating ACME-' + dev.facts['hostname'] + ' | ' + device)
    conf.pdiff()

    if conf.commit_check():
        conf.commit()
    else:
        conf.rollback()

    conf.unlock()
    dev.close()


