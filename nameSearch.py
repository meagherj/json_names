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
    print(data[name]["2017"])
    print(data[name]["2018"])
    print(data[name]["2019"])
    print(data[name]["2020"])
    print(data[name]["2021"])
  except:
    print("Name: "+name+" does not exist in all years")
    
findName("Joseph")
findName("Ethyl")
