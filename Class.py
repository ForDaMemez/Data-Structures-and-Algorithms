class Car():
  # making a constructor which holds the attributes 
  def __init__(self,model,year,colour):
    self.model = model
    self.year = year
    self.colour = colour
# method to display the car details
  def print_info(self):
    print(self.model, self.year, self.colour)
  def change_details(self):
    choice = input("Do you want to change any details")
    if choice == "Yes":
      detail = input("If you want to change the model, press 1. If you want to change the year, press 2. If you want to change the colour,press 3.")
      if detail == "1":
        self.model = input("What do you want to change the model to?")
      elif detail == "2":
        self.year = input("What do want to change the year to?")
      elif detail == "3":
        self.colour = input("What do you want to change the colour to?")
      
# making objects/instances of the class
car1 = Car("Q3","2015","White")
car2 = Car("Model X", "2023", "Black")

car2.change_details()

car2.print_info()
