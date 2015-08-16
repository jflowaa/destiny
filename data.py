class Character:

    def __init__(self, ID, class_hash):
        self.characterID = ID
        self.class_hash = class_hash
        self.class_title = self.get_class_title(class_hash)

    def get_class_title(self, value):
        """
        Matches the hash to the correct text value. If the value is
        not matched, title is set to unknown.
        """
        if value == 671679327:
            return "Hunter"
        elif value == 3655393761:
            return "Titan"
        elif value == 2271682572:
            return "Warlock"
        else:
            return "Unknown Class"

    def create_character_dump():
        """
        Returns the json file of the character.
        """
        return 0


class Account:

    def __init__(self, platform, username, membershipID=0,
                 characterIDs=None, characters=None):
        self.platform = platform
        self.username = username
        self.membershipID = membershipID
        self.characterIDs = []
        self.characters = []

    def set_characerIDs(self, values):
        """
        Sets the found IDs
        """
        for value in values:
            self.characterIDs.append(value)

    def create_character(self, ID, class_hash):
        """
        Creates a character object, passes the ID and hash for instantiation.
        """
        self.characters.append(Character(ID, class_hash))

    def create_account_dump():
        """
        Returns the json file of the account.
        """
        return 0
