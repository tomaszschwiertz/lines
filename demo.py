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
