#!/usr/bin/env python3
import requests
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

url="https://raw.githubusercontent.com/tomaszschwiertz/lines/master/prefix"
read_data = requests.get(url).content.decode('utf8')

print(read_data)


list = read_data.split()
set_command = """
"""


#str="set " + "set ".join(str(i) + "\n" for i in list)


for x in range (0, len(list)):
    set_command+=("set policy-options prefix-list PXL-CUSTOMERS " + list[x] + "\n")

#print (list)
print(set_command)
delete_command = "delete policy-options prefix-list PXL-CUSTOMERS"

#-------------------------accessing PE's







#--------------
U="netconfuser"
P="netconf123"
DEVICES = ["192.0.2.1", "192.0.2.2", "192.0.2.3"]


for device in DEVICES:  # we iterate over all devices in our device list

    dev = Device(device, port=830, user=U, password=P)
    dev.open()

    print('Updating '+dev.facts['hostname']+' | '+device)

    conf = Config(dev)
    conf.lock()
    #conf.load(delete_command, format='set')
    conf.load(set_command, format='set')
    conf.pdiff()
    #config_difference = conf.pdiff()  # todo save and send via e-mail
    #print(config_difference)




    if conf.commit_check():
        conf.commit()
    else:
        conf.rollback()

    conf.unlock()
    dev.close()


