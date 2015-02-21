#neural network library
import neurolab as nl
#other dependancies
import numpy as np
import json

#compute vector representant for network entry
def chaine(str):
	L=[]
	i=0
	for c in str:
		L.insert(i,ord(c)/256)
		i=i+1
		if i==255 :
			break
	for a in range(0,256-len(L)):
		L.insert(i,0)
	return L

#So it name is like, builds the neural network
def buildNetwork():
	L=[]
	for i in range(0,256):
		L.insert(-1,[0,1])
	net = nl.net.newff(L,[5,1])
	return net

#Load Dataset
def readDataset(thefile):
	f=open(thefile)
	inp=[]
	tar=[]
	line=f.readline()
	line=line.rstrip("\n")
	while line!="":
		inp.insert(-1,chaine(line))
		line=f.readline()
		line=line.rstrip("\n")
		tar.insert(-1,[2*((int)(line))-1])
		line=f.readline()
		line=line.rstrip("\n")
	f.close()
	return [inp,tar]


#cheating tricks to build dataset
QUESTION_WORDS = ["Where", "where", "In wh", "How", "Is", "(?,", "What",
        "what", "When", "Qui", "Quel", "qui", "Who", "who", "How", "how"]
MATH_WORDS = ["Integrate", "Limit", "Solve", "Sum", "Derivate", "limit",
        "solve", "sum", "derivate", "integrate", "dsolve", "Dsolve"]
#Build dataset, WARNING manual filling takes lot of time
#Give page logger.frontend.askplatyp.us as entry
#Type 1 for math, 0 otherwise
def buildDataset(loggerinputfile,datasetfile):
	json_data=open(loggerinputfile)
	data = json.load(json_data)
	json_data.close()
	f=open(datasetfile,"w")
	for entry in data :
		f.write(entry[0])
		f.write("\n")
                if any(entry[0].startswith(x) for x in QUESTION_WORDS):
			f.write("0\n")
                elif any(entry[0].startswith(x) for x in MATH_WORDS):
			f.write("1\n")
		else :
			n=input(entry[0])
			f.write(n)
			f.write("\n")
	f.close()

#Just compute output of network with a word
def outputof(net, input):
	return net.sim([chaine(input)])


#net=construireReseau()
#o=lireDataset()

#error=net.train(o[0],o[1],epochs=500, show=10, goal=0.02)

#net.save("network")


