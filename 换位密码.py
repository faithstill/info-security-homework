if __name__ == '__main__':
	input_plaintext=raw_input("please input the plaintext:")
	input_key=raw_input("please input the key(use ','to divide):")
	xkey=input_key.split(",")
	k=0
	ciphertext=[]
	for i in range(0,len(input_plaintext)):
		ciphertext.append(input_plaintext[int(xkey[k])-1])
		k=k+1
		#s_cip=str(ciphertext)
	print "the ciphertext is:  "+"".join(ciphertext)