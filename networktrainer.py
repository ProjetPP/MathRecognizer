import neurolab as nl
import numpy as np
import json

def chaine(str):
    L = [ord(c)/256 for c in str[:256]]
    for i in range(len(L), 256):
        L.append(0)
    return L

def construireReseau():
	L = [(0, 1)] * 256
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

def construireDataset():
	json_data=open('Documents/logger.frontend.askplatyp.us.json')
	data = json.load(json_data)
	json_data.close()
	f=open("testpymath","w")
	for entrie in data :
		f.write(entrie[0])
		f.write("\n")
		if entrie[0].startswith("Where"):
			f.write("0\n")
		elif entrie[0].startswith("where"):
			f.write("0\n")
		elif entrie[0].startswith("In wh"):
			f.write("0\n")
		elif entrie[0].startswith("How"):
			f.write("0\n")
		elif entrie[0].startswith("Is"):
			f.write("0\n")
		elif entrie[0].startswith("(?,"):
			f.write("0\n")
		elif entrie[0].startswith("What"):
			f.write("0\n")
		elif entrie[0].startswith("what"):
			f.write("0\n")
		elif entrie[0].startswith("When"):
			f.write("0\n")
		elif entrie[0].startswith("Qui"):
			f.write("0\n")
		elif entrie[0].startswith("Quel"):
			f.write("0\n")
		elif entrie[0].startswith("qui"):
			f.write("0\n")
		elif entrie[0].startswith("Who"):
			f.write("0\n")
		elif entrie[0].startswith("who"):
			f.write("0\n")
		elif entrie[0].startswith("How"):
			f.write("0\n")
		elif entrie[0].startswith("how"):
			f.write("0\n")
		elif entrie[0].startswith("Integrate"):
			f.write("1\n")
		elif entrie[0].startswith("Limit"):
			f.write("1\n")
		elif entrie[0].startswith("Solve"):
			f.write("1\n")
		elif entrie[0].startswith("Sum"):
			f.write("1\n")
		elif entrie[0].startswith("Derivate"):
			f.write("1\n")
		elif entrie[0].startswith("limit"):
			f.write("1\n")
		elif entrie[0].startswith("solve"):
			f.write("1\n")
		elif entrie[0].startswith("sum"):
			f.write("1\n")
		elif entrie[0].startswith("derivate"):
			f.write("1\n")
		elif entrie[0].startswith("integrate"):
			f.write("1\n")
		elif entrie[0].startswith("dsolve"):
			f.write("1\n")
		elif entrie[0].startswith("Dsolve"):
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


