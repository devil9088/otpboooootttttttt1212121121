import os

from keys import gen
from keys import birthdate

# File path to save the keys
file_path = os.getcwd() + "\\keys.txt"

# Get the keys and write them to a local file
def createkey_local(userid, key, days):
    with open(file_path, "a") as f:
        f.write(f"adminuid: {userid}, date-of-creation: {birthdate()}, date-of-expiration: '', length: {days}, useruid: '', key: {key}\n")


# Generate the keys

# input how many days
days = int(input("How many days? "))
# input how many keys
keys = int(input("How many keys? "))

for i in range(keys):
    key = gen(days)
    print(key)
    createkey_local("5261828597", key, days)

print("Done")
