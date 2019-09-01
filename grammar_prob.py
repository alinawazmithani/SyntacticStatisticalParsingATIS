import nltk
from nltk import tree
from nltk.corpus import treebank
from nltk import treetransforms
from nltk import Nonterminal
from nltk import induce_pcfg
from nltk.parse import pchart

def loadData(path):
	with open(path,'r') as f:
		data = f.read().split('\n')
	return data

def getTreeData(data):
	return map(lambda s: tree.Tree.fromstring(s), data)

# Main script
print("loading data..")
data = loadData('parseTrees.txt')
print("generating trees..")
treeData = getTreeData(data)
print("done!")

productions = []
for trees in treeData:
    # perform optional tree transformations, e.g.:
    trees.collapse_unary(collapsePOS = False)# Remove branches A-B-C into A-B+C
    trees.chomsky_normal_form(horzMarkov = 2)# Remove A->(B,C,D) into A->B,C+D->D
    productions += trees.productions()

S = Nonterminal('S')
grammar = induce_pcfg(S, productions)
#print(grammar)
print()

print("Parse sentence using induced grammar:")

sent = 'show me the meals on the flight from Phoenix'
print(sent)

sent = sent.split(' ')

parser = pchart.InsideChartParser(grammar)
parser.trace(3)

for parse in parser.parse(sent):
    print(parse)


