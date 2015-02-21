import neurolab as nl
import numpy as np
import json

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

def construireReseau():
	L=[]
	for i in range(0,256):
		L.insert(-1,[0,1])
	net = nl.net.newff(L,[5,1])
	return net

def lireDataset():
	f=open("testpymath")
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

QUESTION_WORDS = ["Where", "where", "In wh", "How", "Is", "(?,", "What",
        "what", "When", "Qui", "Quel", "qui", "Who", "who", "How", "how"]
MATH_WORDS = ["Integrate", "Limit", "Solve", "Sum", "Derivate", "limit",
        "solve", "sum", "derivate", "integrate", "dsolve", "Dsolve"]

def construireDataset():
	json_data=open('Documents/logger.frontend.askplatyp.us.json')
	data = json.load(json_data)
	json_data.close()
	f=open("testpymath","w")
	for entrie in data :
		f.write(entrie[0])
		f.write("\n")
                if any(entrie[0].startswith(x) for x in QUESTION_WORDS):
			f.write("0\n")
                elif any(entrie[0].startswith(x) for x in MATH_WORDS):
			f.write("1\n")
		else :
			n=input(entrie[0])
			f.write(n)
			f.write("\n")
	f.close()


def outputof(net, input):
	return net.sim([chaine(input)])


#net=construireReseau()
#o=lireDataset()

#error=net.train(o[0],o[1],epochs=500, show=10, goal=0.02)

#net.save("network")


