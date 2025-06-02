from passlib.hash import des_crypt

def test_pass(crypt_pass):
	salt = crypt_pass[:2] #Extract the salt from the hash; the first 2 characters of the hash
	with open('dictionary.txt', 'r') as dict_file:
		for word in dict_file:
			word = word.strip('\n') #remove new line characters if any
			crypt_word = des_crypt.hash(word, salt=salt)
			if crypt_word == crypt_pass:
				print(f"[+] Found Password: {word}\n")
				return
	print("[-] Password Not Found. \n")

def main():
	with open('passwords.txt', 'r') as pass_file:
		for line in pass_file:
			if ":" in line:
				user, crypt_pass = line.strip().split(':')
				print(f"[*] Cracking Password For: {user}")
				test_pass(crypt_pass)

if __name__ == "__main__":
	main()
