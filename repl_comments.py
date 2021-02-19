#I borrowed some code from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py (from line 5 to line 9)

liste = []

from hashlib import sha256

def create_hash(password):
    pw_bytestering = password.encode()
    return sha256(pw_bytestering).hexdigest()

my_password = "fsafsa"
my_hash = create_hash(my_password)

while True:

    comment = input("Enter your comment:")
    user_password = input("Enter your password:")
    user_hash = create_hash(user_password)

    if my_hash == user_hash:

        liste.append(comment)

        print("Previously entered comments:")

        for x in liste:
            i = 1 + liste.index(x)
            print(str(i) + "." + x)
    else:
        print("Wrong password. I can't let you do that.")

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
