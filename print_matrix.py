import pickle
fi = open("matrix.data", "rb")
fi.seek(0)
m = pickle.load(fi)
fi.close()

for i in m:
	print i 
	print "\n"