
cities={} # An empty dict

myFile=open("cities.txt")

for line in myFile:
    city,temp=line.split(":") #unpacking is used
    temp=float(temp)
    cities[city]=temp # a new element is added to the dict cities
    
print(cities)   

print("temperature of gimel:", cities["gimel"])
print("temperature of lausanne:", cities["lausanne"])

myFile.close()