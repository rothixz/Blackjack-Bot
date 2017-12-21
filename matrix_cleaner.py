import pickle

m = [[[  ["h",10,10],["s",10,10]  ] for i in range(22)] for j in range(22)]

for i in range(22):
	for j in range(22):
		print m[i][j] 
		print "\n"



###
#Escrever matrix de persistencia
###
fo = open( "matrix.data", "wb" ) 
fo.seek(0)
fo.truncate()
fo.seek(0)
pickle.dump( m, fo)
fo.close()