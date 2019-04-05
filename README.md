# 310-Software-Engineering

Welcome to the world enriched by the wonderful TherapistJen!
Therapist Jen is here as a companion to help you work through negative feelings and thoughts, and help you work towards your positive goals!

Disclaimer: TherapistJen is a tool meant to help encourage positive behaviour and is designed to work alongside other methods such as professional therapy.


#Compiling and Running TherapistJen

To compile and run TherapistJen, one must first be either on the UBC Okanagan campus and connected to an official UBC network, or connected to myvpn.ok.ubc.ca. This will allow TherapistJen to access her database or responses. 

When running TherapistJen, first run the "TherapistJen.py" file and then follow the hyperlink address that is generated in the terminal. This will bring you to TherapistJens's chatroom.

Proceed to use TherapistJen to aid you in the maintenence of your mental health.




#Dependencies:
re, cherrypy, pyodbc, spacy, tensorflow, keras, numpy

#Components:
The functionality of the program is divided into four sections:

Web-based Platform Use - located in the "static" folder

Natural Language Processing - located in the "NLP" folder, this is used to process the user input into usable data.

Neural Network - based Machine Learning - located in the "NN+Support" folder, this is used to associate the useable data from the NLP with the feelings of the one writing the input

SQL Database Queries - located in the "JenDatabaseQueryTechniques.py" file, this is used to access the database of responses that TherapistJen has available.


#Classes:
parsingStringFunction.negativeThoughtsOrGoals(userMessage) - returns 'negative' or 'goals' as the user responds to TherapistJen.

parsingStringFunction.questionOrStatement(userMessage) - determines if the userMessage is a question or a statement and returns 'question' or 'statement'.

NLP_For_Training.main(userInput) - analyses the userInput and returns a matrix counting the presneces of each flagged word. Formatted for use as input for the Neural Network.

JenDatabaseQueryTechniques.getResponse(sOrQ, feeling, subject, questionNum) - uses input to query the SQL database for the appropriate response.

JenDatabaseQueryTechniques.searchStringFor(userMessage, synonym) - searches userMessage for synonym and returns true if the synonym is contained within userMessage. Return false otherwise.

JenDatabaseQueryTechniques.getFeeling(userMessage) - associates userMessage with a catagory of feeling. Returns string.

neural_net_response.getResponse(sOrQ,userInput, subject, questionNum) - uses input to query the SQL database for the appropriate response using the neural net

EntityRecognition.java - uses openNLP in order to recognize named entities from the user input

Synonyms.py - uses wordnet, and natural language toolkit in order to generate a large number of keywords that we can use for processing emotion

wordProcess.py - readies the entity recognition functions and the preprocessed synonyms

porterStemmer.py - applies the porter stemmer algorithm to generify user input

Implemented features since assignment 2:
  - Entity recognition
      - finds named entities in user input so they aren't considered for keywords (for example ("Dead Sea") will be recognized as an             entity and therefore the 'Dead' keyword won't be called)
      - https://imgur.com/a/oUKLFUR <- Can be seen here, Therapist Jen respects no keyword even though "dead" is normally a keyword for suicidal, as "Dead Sea" is recognized as a named entity
  - Synonym finding
      - uses the openNLP database to find synonyms for our keywords (rather than an assortment of hand picked keywords, we used a               database to find a broader amount)
      - https://imgur.com/a/pITdkM2 <- Can be seen here, 'void' was previously not a keyword in the older version, it has been added using a synoynym finding algorithm and 'NLP'
  - Porter Stemmer
    - Removes endings to words, generifiying them, for example, 'lacking' will be generified to 'lack' for the purpose of gathering keywords
    - https://i.imgur.com/v2tCU0e <- Porter stemmer turns 'lacking' to 'lack' which is a keyword associated with emptiness




