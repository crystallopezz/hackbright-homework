"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for melon, details in melons.items():
        print(melon.upper())
        for detail, value in details.items():
            print (detail, value)
