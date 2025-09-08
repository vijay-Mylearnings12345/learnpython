class Laptop:
    def __init__(self,model,size,price,make_year,availability):
        self.model = model
        self.size = size
        self.price = price
        self.make_year = make_year
        self.availability = availability

    def booting_time(self):
        print("The laptop1 is having the good booting speed time")

    def shutdown_time(self):
        print(f"The {self.model} is not having the good shutdown time")