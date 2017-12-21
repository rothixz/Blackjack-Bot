#!/usr/bin/python

overall_sum = 0
n = 0

f = open("teste.txt", "r")

for line in f:
	xd = line[15:line.find(")")-3]
	xd = int(xd)
	print xd
	overall_sum += xd
	n += 1
print float(overall_sum) / n