import numpy as np
import sys
def check_for_interlinks(adj):
	for r in range(total):
		for c in range(total):
			if (r/nn != c/nn):
				if (a[r][c] != 0):
					return True
	return False
def Create_Tensor(flag):
	if(flag):
		print ('Interlinks')
		f = s = th = la = 0
		for p in range(total):
			for q in range(total):
				f = p % nn
				s = q % nn
				th = q / nn
				la = p / nn
				ti[f][s][th][la] = a[p][q]
				#print str([f,s,th,la]) + str(ti[f][s][th][la]),
				#print '\n'
		Display_Tensor(True)
	else:
		print ('Intralinks Only')
	# array intralink display
		for i in range(total):
			for j in range(total):
				x = l = i / nn
				y = j / nn	
				if (x == y):
					f = i % nn
					s = j % nn
					t[f][s][l] = a[i][j]
	# Display Tensor
		Display_Tensor(False)
def Display_Tensor(flag):
	if (flag):
		for la in range (nl):
			for sl in range (nl):
				for fl in range (nn):
					print '/' + '',
					for tl in range (nn):
						print str(ti[fl][tl][sl][la]) + '',
						#print '\n'
					print '/'
					print '\n'
				print '\n'	
	else:
		for z in range (nl):
			for x in range (nn):
				print '/' + '',
				for y in range (nn):
					print str(t[x][y][z]) + '',
				print '/'
				print '\n'
			print '\n'	
filename = sys.argv[1]
file = open(filename, "r")
lines = []
nn = nl = n = l = 0
for line in file:
	parts = line.split()
	if parts[0] == "Nodes":
		n = parts[1]
	elif parts[0] == "Layers":
		l = parts[1]
	else:
		lines.append(parts)
nn = int(n)
nl = int(l)
total = nn*nl
a = np.zeros((total,total))
t = np.zeros((nn, nn, nl))
ti = np.zeros((nn, nn, nl , nl))
for r in range(total):
	for c in range(total):
		a[r][c] = lines[r][c]
flag = check_for_interlinks(a)
Create_Tensor(flag)