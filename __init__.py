from query_api import QueryAPI
from sys import argv

data = QueryAPI(argv[1], argv[2])

print("Membership ID: {}".format(data.account.membershipID))
print("Characer(s) on this account are: ")

for characer in data.account.characters:
    print("\tID: {}".format(characer.characterID))
    print("\tClass hash: {}".format(characer.class_hash))
    print("\tClass title: {}\n".format(characer.class_title))
