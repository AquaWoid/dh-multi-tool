import pandas 
from matplotlib import pyplot
import sys, os

j = {
  "0": {
    "id": 0,
    "name": "string",
    "price": 120,
    "date": "string",
  },
  "1": {
    "id": 1,
    "name": "string",
    "price": 2220,
    "date": "string",
  },
  "2": {
    "id": 2,
    "name": "string",
    "price": 340,
    "date": "string",
  }
}

path = os.path.dirname(os.path.join(sys.path[0], "Datasets", "scuola.CSV"))

pathdebug = r"C:\Users\luwa0\Documents\Repos\dh-multi-tool\Backend\Datasets\scuola.CSV"


#file = open (pathdebug, mode="r", encoding="utf-8")

df = pandas.read_csv(pathdebug, encoding="ISO-8859-15", sep=";", on_bad_lines="skip")

#print(df["DATE"])

print(df.groupby(["NOME"]).all())

#df.to_csv(os.path.join(sys.path[0], "test.csv"), sep=";")

"""
pyplot.bar(data=df.groupby())
pyplot.show()

#print(df["price"])
"""




def plotFromJson():
    return None

def plotFromCsv():
    return None