import random, csv
from typing import TypedDict

Feature = TypedDict("Feature", {"cost":int, "value":int})
FeatureSet = TypedDict("FeatureSet", {"id":int, "feature":Feature})

def gen_features(n):
    with open("nrp_{}.csv".format(n), "w") as f:
        f.write("id,cost,value\n")
        for i in range(100):
            cost = random.randrange(1000, 8000, 50)
            value = random.randrange(100, 1000, 10)
            f.write("{},{},{}\n".format(i, cost, value))
    
# gen_features(100)

def read_data(filename:str):
    features = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            features[int(row["id"])] = {"value":int(row["value"]), "cost":int(row["cost"])}
    return features

class Solution:
    def __init__(self, features:FeatureSet):
        self.features = features
        self.solution = [0] * len(features)    

    def __str__(self):
        return "{}, cost: {}, value: {}".format(self.indices(), self.cost(), self.value())
    
    def copy(self):
        new = Solution(self.features)
        new.solution = self.solution[:]
        return new

    def randomize(self):
        self.solution = []
        for i in range(len(self.features)):
            self.solution.append(random.randrange(0, 2))

    def indices(self):
        return [i for i in range(len(self.features)) if self.solution[i] == 1]

    def size(self):
        return len(self.features)

    def cost(self):
        return sum(self.features[i]["cost"] for i in range(len(self.features)) if self.solution[i] == 1)
    
    def value(self):
        return sum(self.features[i]["value"] for i in range(len(self.features)) if self.solution[i] == 1)

    def add(self, index):
        self.solution[index] = 1
    
    def remove(self, index):
        self.solution[index] = 0

    