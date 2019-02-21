import numpy as np
import sys
def create_Tensor(f):
	counter = 0
	# Tensor for Interlinks
	if(f):
		for i in range(nr):
			counter = counter + 1
			for j in range(nn):
				f = i % nn
				s = j
				l = i / (nn*nl)
				if (counter % (nn * nl) == 0):
					counter = 0
				else:
					pass
				th = counter / nn	
				ti[f][s][th][l] = lines[i][j]
				#print (str([f , s, th, l]) + str(ti[f][s][th][l]))
	else:
	# Tensor for Intralinks
		for i in range(total):
			for j in range(nn):
				f = i % nn
				s = j 
				th = i / nn
				t[f][s][th] = lines[i][j]
def Create_Adj_From_Tensor(fl):
	# For Interlinks 
	if (fl):
		for f in range(nl):
			for th in range (nl):
				for i in range (nn):
					for j in range(nn):
						ai = i + f * nn
						aj = j + th * nn
						a[ai][aj] = ti[i][j][th][f]
		print('Interlink Adjacency Matrix Done')
	# For Intralinks
	else:
		for l in range (nl):
			for i in range(nn):
				for j in range(nn):
					ai = l * nn + i
					aj = l * nn + j
					a[ai][aj] = t[i][j][l]				
def Display_Matrix(a):
	for i in range(total):
		for j in range(total):
			print str(a[i][j]) + ' ',
		print ''
	print ('\n')			
def check_for_interlinks(r):
	if(r == nn*nl*nl):
		print('Interlinks are present and Network is Multiplex Network')
		return True
	elif(r == nn*nl):
		print('Only Intralinks are present and Network is Multilayer Network')
		return False
filename = sys.argv[1]
file = open(filename, "r")
lines = []
nn = nl = n = l = li = nr = 0
flag = True
for line in file:
	parts = line.split()
	if parts[0] == "Nodes":
		n = parts[1]
	elif parts[0] == "Layers":
		l = parts[1]
	else:
		lines.append(parts)
		nr = nr + 1
#print ('Total Lines in file are' + str (nr))
nn = int(n)
nl = int(l)
total = nn*nl
a = np.zeros((total,total))
t = np.zeros((nn,nn,nl))
ti = np.zeros((nn,nn,nl,nl))
flag = check_for_interlinks(nr)
create_Tensor(flag)
Create_Adj_From_Tensor(flag)
Display_Matrix(a)