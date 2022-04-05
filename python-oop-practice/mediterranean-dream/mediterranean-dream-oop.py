# Mediterranean Dream OOP practice project
# Overview of room options
# basic double room,
# suite,
# single room,
# shared room in girls only and boys only rooms

# Other services
# breakfast service
# sauna service
# pool service
# spa service

# Customers can book as many services as they wish

# 1. create room class

class Room:
    def __init__(self, price, size):
        self.price = price
        self.size = size

    def bookroom(self):
        print("You can book this " + self.size + " room for $" + str(self.price) + " per night.")


studio = Room(60, "studio")
studio.bookroom()


# 2. exploit inheritance

class Suite(Room):
    pass

    # def booksuite(self):
    #   print("You can book this " + self.size + " room for $" + str(self.price) + " per night.")
    # should not have to make this method again? inherited from the Room class


suite1 = Suite(90, "Suite")
suite1.bookroom()


class Shared(Room):
    pass

# 3. inherit from class Shared, with more attributes
