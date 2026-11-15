# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated
        if not isinstance(pounds, int) or not isinstance(pence, int):
            raise TypeError("Pounds and pence must be integers")

        if pounds < 0:
            raise ValueError("Pounds cannot be negative")

        if pence < 0 or pence > 99:
            raise ValueError("Pence must be between 0 and 99")
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds}.{self.pence:02d}"
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        if not isinstance(other, Money):
            raise TypeError("Can only add Money objects")

        pounds = self.pounds + other.pounds
        pence = self.pence + other.pence

        pounds = pounds + pence // 100
        pence = pence % 100

        return Money(pounds, pence)
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
