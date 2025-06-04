import zipfile
zFile = zipfile.ZipFile("dummy.zip")
zFile.extractall(pwd ="secre".encode())
