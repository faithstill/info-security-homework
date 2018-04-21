import sys
defaultencoding = 'utf-8'
def yaokong(plaintext,len1,num):
	k=num-1
	len_plaintext=len(plaintext)
	tem_s=[]
	while (k < len_plaintext-1) or (k == len_plaintext-1):
		tem_s.append(plaintext[k])
		k=k+len1
	return "".join(tem_s)
if __name__ == '__main__':
	alphabet=[chr(i) for i in range(97,123)]
	input_plaintext=raw_input("please input the plaintext:")
	input_key=raw_input("please input the key:")
	len_key=len(input_key)
	tem=0
	for i in alphabet:
		#print i
		for k in input_key:
			tem=tem+1
			if k==i:
				#print tem
				print yaokong(input_plaintext,len_key,tem)
				print "\n"
		tem=0
