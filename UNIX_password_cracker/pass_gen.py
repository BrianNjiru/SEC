from passlib.hash import des_crypt

users = {
	"alice": "apple",
	"bob": "banana",
	"carol": "cherry"
}

salt = "ax"
with open("passwords.txt", "w") as f:
	for user, pw in users.items():
		hashed_pw = des_crypt.hash(pw, salt=salt)
		f.write(f"{user}:{hashed_pw}\n")
