class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year: ", self.year,  ". City: ", self.city)


school = Building(2000, 'Moscow')
house = Building(2000, 'San Francisco')
shop = Building(2000, 'San Francisco')