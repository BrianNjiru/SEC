import zipfile
zFile = zipfile.ZipFile("dummy.zip")
zFile.extractall(pwd ="secret".encode())
