"""
Given a file like the following:
    lausanne:6.3
    geneve:3.2
    nyon:4.3
    lausanne:7.3
    geneve:3.7
    nyon:2.3
    lausanne:5.3
    geneve:5.2
    nyon:2.3
    
makes use of it the create a dict like this one:
    
    {
     "lausanne":[6.3,7.3,5.3],
     "geneve":[3.2,3.7,5.2],
     "nyon":[4.3,2.3,2.3]
     }
    
then use the dict to find the average of the temperature associated with a 
given city name.

Note: to simplify the code you can assume the file format is "correct"
"""
cities={} # An empty dict

myFile=open("cities.txt")

for line in myFile:
    city,temp=line.split(":") #unpacking is used
    temp=float(temp)
    if city in cities:
        cities[city].append(temp)
    else:
        cities[city]=[temp] # a new element is added to the dict cities

myFile.close()

cityName=input("Enter a city name:")
if cityName in cities:
    print(f"Average of the temperature of {cityName} is {sum(cities[cityName])/len(cities[cityName])}")
else:
    print(f"{cityName} is not in my dict!")
    print("Existing cities name are:", list(cities.keys()))

