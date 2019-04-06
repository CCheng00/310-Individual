import py4j
from py4j.java_gateway import JavaGateway
import porterStemmer

def trim(userInput):
    if(userInput == "Negative Thoughts"):
        return userInput
    value = userInput
    try:
        gateway = JavaGateway()
        entityRecognition = gateway.entry_point
        value = entityRecognition.trimmer(userInput)
    except:
        value = userInput

    output = porterStemmer.psstem(value)
    return output

def synList():
    output = {}
    count = 0
    with open("associations.txt") as f:
        for line in f:
            words = line.split()
            key = words[0]
            vals = []
            for i in range(1, len(words)):
                vals.append(words[i])
            output[key] = vals
            count = count+1

    return output







