#Crypt is deprecated
import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2] #Extract the first  2 characters as the salt
	dictfile = open('dictionary.txt', 'r')
	for word in dictfile.readlines(): #Loop through each word in the dictionary
		word = word.strip('\n') #Remove newline character
		cryptWord = crypt.crypt(word.salt) #Hash the word from the dictionary with the same salt used to hash the password.
		if (cryptWord == cryptPass): #compare hashes
			print ("[+] Found Password: "+word+"\n") # Alert user when match is found
			return
	print ("[-] Password Not Found. \n") # Match not found
	return

def main():
	passFile = open('passwords.txt') #Read the encrypted passwords file
	for line in passFile.readlines(): #each line contains a username and a password
		if ":" in line: #This if function formats lines; username:password-hash
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print ("[*] Cracking Password For: "+user)
			testPass(cryptPass)

if __name__ == "__main__":
	main()
