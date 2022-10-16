import json

file = open ("names.json")
data = json.load(file)

def findName(name):
  try:
    tryName = data[name]
  except:
    print("Can't find name")
  try:
    print(data[name]["2017"])
    print(data[name]["2018"])
    print(data[name]["2019"])
    print(data[name]["2020"])
    print(data[name]["2021"])

findName("Joseph")
findName("Ethyl")
findName("None")
