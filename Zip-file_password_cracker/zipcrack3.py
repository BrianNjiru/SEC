import zipfile

def extract_file(zFile, password):
        try:
                zFile.extractall(pwd = password.encode('utf-8'))
                return password
        except:
                return

def main():
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



