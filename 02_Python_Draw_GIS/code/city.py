# City class - contains name, location, and populatin
class City():
    # Constructor
    def __init__(self, data):
        # data is in form [c, name, x position, y position, population]
        self.name = data[1]
        self.x = float(data[2])
        self.y = float(data[3])
        self.loc = (self.x, self.y)
        self.pop = int(data[4])

# new_city = City([c,Astoria,-133.996669,190.000000,9500])
# new_city = City(['c,Astoria,-133.996669,190.000000,9500'])
# new_city = City(['c','Astoria',-133.996669,190.000000,9500])
# print(new_city.name)
