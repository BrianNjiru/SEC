import zipfile
import optparse
from threading import Thread

def extract_file(zFile, password):
        try:
                zFile.extractall(pwd = password.encode('utf-8'))
                return password
        except:
                return

def main():
	parser = optparse.OptionParser("usage%prog " +\ "-f <zipfile> -d <dictionary>")
	parser.add_option('f', dest = 'zname', type = 'string',\help='specify zip file')
	parser.add_option('-d', dest = 'dname', type = 'string', \help = 'specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname




        zFile = zipfile.ZipFile('dummy.zip')
        passfile = open('dictionary.txt')
        for line in passfile.readlines():
                password = line.strip('\n')
                print(f"[*] Trying password: {password}\n")
                guess = extract_file(zFile, password)
                if guess:
                        print (f'[+]Password = {password} \n')
                        exit(0)

if __name__ == '__main__':
        main()



