import pyodbc
import re
import wordProcess

server = "sql04.ok.ubc.ca"
database = "db_jlabossi"
username = "jlabossi"
password = "23976160"


feelingType = wordProcess.synList()



def getResponse(sOrQ, feeling, subject, questionNum):
    if questionNum <= 30:
        cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database, user=username, password=password)
        cursor = cnxn.cursor()
        if sOrQ == "question":
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'question\'')
        else:
            cursor.execute('SELECT response FROM ChatBot WHERE sOrQ = \'statement\' AND questionNum = \'' + str(questionNum) + '\'AND feeling = \'' + feeling + '\' AND subject = \'' + subject + '\'')
        for row in cursor:
            return row[0]

def searchStringFor(userMessage, synonym):
    matchAsRegex = re.search(synonym, userMessage)
    return bool(matchAsRegex)

def getFeeling(userMessage):
    for feeling in feelingType :
        synonyms = feelingType.get(feeling, "default")
        for synonym in synonyms:
            if searchStringFor(userMessage, synonym):
                return feeling
    return "nothing"

