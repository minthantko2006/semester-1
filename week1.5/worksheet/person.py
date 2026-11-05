# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth) :
        """ Create a person with a name and date of birth """

        if not isinstance(name, str) :
            raise TypeError("Name is not a string")
        if name == "":
            raise ValueError("Name is an empty string")
        if not isinstance(birth, date) :
            raise TypeError("Birth is not a date")

        self.name = name
        self.birth = birth



    # Implement methods initials() and is_birthday() here

    def initials(self) :
        """ Return the uppercased initial letters of each part of person's name"""
        result = ""
        for part in self.name.split():
            result = result + part[0].upper()
        return result

    def is_birthday(self):
        """ Return True if today is the person's birthday"""
        today = date.today()
        if self.birth.month == today.month and self.birth.day == today.day :
            return True
        else:
            return False

    # (see README.md for further details)
