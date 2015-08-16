from data import Account
import requests


class QueryAPI:
    BASE_URL = 'http://www.bungie.net/Platform/Destiny/'
    match = []

    def __init__(self, platform, username):
        self.account = Account(platform, username)
        self.mine_data()

    def mine_data(self):
        self.get_membershipID()
        self.get_characterIDs()
        self.get_class_hash()
        return

    def get_membershipID(self):
        """
        Gets the membershipID, stores the value in the Account object.
        """
        response = requests.get(self.BASE_URL + self.account.platform +
                                "/Stats/GetMembershipIdByDisplayName/" +
                                self.account.username)
        self.account.membershipID = response.json()['Response']

    def get_characterIDs(self):
        """
        Gets the character IDs. This returns a large amount of data via json.
        search_data() method is used to parse for IDs. Values are stored in
        the Account object.
        """
        response = requests.get(self.BASE_URL + self.account.platform +
                                "/Account/" + self.account.membershipID)
        self.search_data(response.json(), "characterId")
        self.account.characterIDs = self.match
        self.clear_match()

    def get_class_hash(self):
        """
        Gets the class hash(es) for each character found. Uses search_data()
        to parse. After all the class hash(es) are found, create_characters
        is called in the Account object.
        """
        for charID in self.account.characterIDs:
            response = requests.get(self.BASE_URL + self.account.platform +
                                    "/Account/" + self.account.membershipID +
                                    "/Character/" + str(charID))
            self.search_data(response.json(), "classHash")
            self.account.create_character(str(charID), self.match[0])
            self.clear_match()

    def search_data(self, data, searched_key):
        """
        Parses the return json file. data is the json object(dict).
        searched_key is the key that you want found.
        EXAMPLE: a searched_key = "classHash" will return all the values
        of any key(s) found with that value. Issue with recursion. If
        returning muiltple values, the results are in the match list.
        """
        found = []
        for key, value in data.items():
            if key == searched_key:
                found.append(value)
            elif isinstance(value, dict):
                self.search_data(value, searched_key)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.search_data(item, searched_key)
        if found:
            if found not in self.match:
                self.match.extend(found)
        return found

    def clear_match(self):
        """
        Clears the list match of any of the results stored from last query.
        """
        self.match = []
