def vigenere(plaintext,key):
	alphabet=[chr(i) for i in range(97,123)]
	alphabet=alphabet+alphabet
	plaintext_ord=ord(plaintext)-97
	k=ord(key)-97
	return alphabet[k+plaintext_ord]
if __name__ == '__main__':
	input_plaintext="lovethenortheasternuniversityverymuch"
	input_key="wz"
	ciphertext=[]
	while len(input_key)<len(input_plaintext):
		input_key=input_key+input_key
	for i in range(0,len(input_plaintext)):
		ciphertext.append(vigenere(input_plaintext[i],input_key[i]))
	print "the ciphertext is:  "+"".join(ciphertext)