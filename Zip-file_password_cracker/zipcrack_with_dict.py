import zipfile

# Load zip file
zFile = zipfile.ZipFile('dummy.zip')

# Open password dictionary
with open('dictionary.txt', 'r') as passFile:
    for line in passFile:
        password = line.strip()  # Remove any newline or trailing spaces
        print(f"[*] Trying password: {password}")
        try:
            zFile.extractall(pwd=password.encode('utf-8'))  # Encode as bytes
            print(f'[+] Password found: {password}\n')
            break  # Exit the loop once password is found
        except Exception as e:
            # Optional: print the error for debugging
            # print(f"[-] Incorrect password: {password} ({e})")
            continue

