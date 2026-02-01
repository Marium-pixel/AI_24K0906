#q.1

class Vehicle:
  def __init__(self,vehicle_id,brand,rent_per_day):
    self.vehicle_id=vehicle_id
    self.brand=brand
    self.rent_per_day=rent_per_day
  def display_details(self):
    print("vehicle ID:", self.vehicle_id)
    print("brand:", self.brand)
    print("Rent per day: $", self.rent_per_day)
  def calculate_rent(self,days):
    rent = days * self.rent_per_day
    print("rent is: $", rent)

V1 = Vehicle(673894,"Volkswagon",25)
V2 = Vehicle(374743,"Mercedez",150)

V1.display_details()
V1.calculate_rent(10)
V2.display_details()
V2.calculate_rent(5)
