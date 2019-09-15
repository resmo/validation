import json


class MessageBag:

    items = {}

    def add(self, error, message):
        """Adds an error and message to the message bag

        Arguments:
            error {string} -- The error to add
            message {string} -- The message to add
        """

        if error in self.items:
            self.items[error].append(message)
        else:
            self.items.update({error: [message]})

    def all(self):
        """Get all errors and messages
        """
        return self.items

    def any(self):
        """If the messagebag has any errors
        """
        return len(self.items) > 0

    def empty(self):
        """If the messagebag has any errors
        """
        return not self.any()

    def first(self):
        """Gets the first error and message
        """
        for key, value in self.items.items():
            return {key: value}

    def count(self):
        """Gets the amount of errors
        """
        return len(self.items)

    def json(self):
        """Gets the amount of errors
        """
        return json.dumps(self.items)

    def amount(self, key):
        """Gets the amount of messages

        Arguments:
            key {string} -- the error to get the amount of.

        Returns:
            int -- Returns the amount of messages
        """
        return len(self.items[key])

    def get(self, key):
        """Gets all the messages for a specific error
        """
        return self.items[key]

    def errors(self):
        """Gets a list of errors
        """
        return list(self.items.keys())

    def messages(self):
        """Gets a list of all the messages
        """
        messages = []
        for error, message in self.items.items():
            messages += message

        return messages

    def reset(self):
        """Gets a list of all the messages
        """
        self.items = {}

    def merge(self, dictionary):
        """Gets a list of all the messages
        """
        self.items.update(dictionary)
        return self.items