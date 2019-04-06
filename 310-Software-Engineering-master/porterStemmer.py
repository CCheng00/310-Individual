from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')
ps = PorterStemmer()

def psstem(input):
    output = ""
    words = word_tokenize(input)
    for w in words:
        temp = ps.stem(w)
        output = output + temp + " "
    return output

