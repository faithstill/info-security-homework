even =[]
odd =[]
if __name__ == '__main__':
	input=raw_input("please input the password your want to encrypt:")
	for i in range(0,len(input)):
		if i%2 == 0 :
			even.append(input[i])
		else :
			odd.append(input[i])
	print "the ciphertext is :"+"".join(even)+" "+"".join(odd)