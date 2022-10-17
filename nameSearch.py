import json

file = open ("names.json")
data = json.load(file)

def findName(name):
  try:
    tryName = data[name]
  except:
    print("Can't find name:"+name)
    return
  try:
    print(name+ " 2017:"+ str(data[name]["2017"]))
    print(name+ " 2018:"+ str(data[name]["2018"]))
    print(name+ " 2019:"+ str(data[name]["2019"]))
    print(name+ " 2020:"+ str(data[name]["2020"]))
    print(name+ " 2021:"+ str(data[name]["2021"]))
  except:
    print("Name: "+name+" does not exist in all years")
    
findName("Joseph")
findName("Ethyl")
findName("Local")
findName("Joe")
findName("Rishi")

findName("Jeoff")
findName("Michelle")
