import zipfile
import threading
import argparse

def extract(zip_file, password):
	try:
		zip_file.extractall(pwd=password.encode())
		print(f"[+] Password found: {password}")
	except:
		pass

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("zipfile", help="Path to zip file")
	parser.add_argument("wordlist", help="Path to wordlist")
	args = parser.parse_args()

	zip_file = zipfile.ZipFile(args.zipfile)
	with open(args.wordlist, "r") as f:
		for line in f:
			password = line.strip()
			t = threading.Thread(target=extract, args=(zip_file, password))
			t.start()

if __name__ == "__main__":
	main()
