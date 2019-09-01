import nltk
from nltk.corpus import treebank

# here we load in the sentences
# here we define a grammar
grammar = nltk.CFG.fromstring("""
S -> NP VP | Aux NP VP | VP | IVP
NP -> Pronoun | Proper-Noun | Det Nom | NP PP
Nom -> Noun | Nom Noun | Nom PP
VP -> Verb | Verb NP | Verb NP PP | Verb PP | VP PP 
PP -> Prep NP 
Det -> 'that' | 'this' | 'the' | 'a'
Noun -> 'book' | 'flight' | 'meal' | 'money' | 'seats'
Verb -> 'book' | 'include' | 'prefer'
Pronoun -> 'I' | 'she' | 'me'
Proper-Noun -> 'Houston' | 'NWA' | 'Denver'
Aux -> 'does'
Prep -> 'from' | 'to' | 'on' | 'near' | 'through'
IVP -> IVerb NP NP | IVerb NP NP PP
IVerb -> 'List'
""")    

# here we let nltk construct a chart parser from our grammar
parser = nltk.ChartParser(grammar)

# input: a list of words
# returns all the parses of a sentence
def allParses(sentenceList):
	return parser.parse(sentenceList)

# input: a list of parse trees
# prints all the parse trees
def printParses(parses):
    for tree in parses:
        print(tree)
        #print(tree.draw())

# input: a sentence as a string or as a list of words
# prints a sentence, then parses it and prints all the parse trees
def processSentence(sentence):
	sentenceList = sentence
	if isinstance(sentence,str):
		sentenceList = sentence.split(' ')
	print('Original sentence: ' + ' '.join(sentenceList))
	printParses(allParses(sentenceList))

def mainScript():
    processSentence('List me the seats on the flight to Denver')

mainScript()
