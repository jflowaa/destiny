# Destiny API Testing in Python

Writing for learning purposes, later to be used in a flask app.

Currently only searches for account ID, and character ID, hashes/title.

To run this program:

> python __init__.py `platform` `account name`
>> Where `platform` is either 1 for xbox or 2 for playstation, and `account name` is your gammertag.

This will build a query_api object, and that builds an account and character object. It'll then populate those classes with data.

For example to access this data:
```python
data = QueryAPI(argv[1], argv[2])

print("Membership ID: {}".format(data.account.membershipID))
print("Characer(s) on this account are: ")

for characer in data.account.characters:
    print("\tID: {}".format(characer.characterID))
    print("\tClass hash: {}".format(characer.class_hash))
    print("\tClass title: {}\n".format(characer.class_title))
```
