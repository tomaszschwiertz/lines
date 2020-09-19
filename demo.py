import requests



url="https://raw.githubusercontent.com/tomaszschwiertz/lines/master/prefix"
read_data = requests.get(url).content.decode('utf8')

print(read_data)


list = read_data.split()
str3 = """
"""


#str="set " + "set ".join(str(i) + "\n" for i in list)


for x in range (0, len(list)):
    str3+=("set "+list[x] + "\n")

#print (list)
print(str3)

#-------------------------accessing PE's

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

#login parameters
r1u = "ops"
r1p = "Opsops"
r1ip = "172.16.0.0"

dev = Device (host=r1ip, port=830, user=r1u, password=r1p)
dev.open()
conf = Config(dev)
conf.lock()
conf.load(str3, format='set')
conf.pdiff()
config_difference = conf.pdiff() #todo save and send via e-mail

if conf.commit_check():
    conf.commit()
else:
    conf.rollback()

conf.unlock()
dev.close()




#--------------
U="netconf"
P="netconf123$"
DEVICES = ["172.16.0.0", "172.16.0.1"]

for device in DEVICES:  # we iterate over all devices in our device list

    dev = Device(DEVICES[device], port=830, user=U, password=P)
    dev.open()
    conf = Config(dev)
    conf.lock()
    conf.load(str3, format='set')
    conf.pdiff()
    config_difference = conf.pdiff()  # todo save and send via e-mail

    if conf.commit_check():
        conf.commit()
    else:
        conf.rollback()

    conf.unlock()
    dev.close()
