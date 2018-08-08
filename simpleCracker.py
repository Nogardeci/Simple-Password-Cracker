import hashlib

def tryPass(encryptedPass):
	dictFile = open('passwords.txt', 'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		encryptedWord = hashlib.sha512(str(word).encode('utf-8')).hexdigest()
		if (encryptedWord == encryptedPass):
			print ("Password Found: "+word+"\n")
			return
	print ("Could not find password in dictionary. \n")
	return

def main():
	passFile = open('victim.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			encryptedPass = line.split(':')[1].strip(' ')
			print ("Cracking password for: " + user)
			tryPass(encryptedPass)

if __name__ == "__main__":
	main()
