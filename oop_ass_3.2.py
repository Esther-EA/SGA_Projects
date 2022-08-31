#create a class called car

class Car:
    def __init__(self, color, brand, model, year, body):
        
        #give five attributes of hte car class
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year
        self.body_type = body
        
#give five mothods of the car clss
    def car_color(self):
        return(f'The color of my car is {self.color}')
    
    def car_brand(self):
        return self.brand
    
    def car_model(self):
        return self.model
    
    def car_year(self):
        return self.year
    
    def car_body_type(self):
        return(f'it is a {self.body_type}')
    
My_first_car = Car('silver', 'Toyota', 'Camry', '2013', 'sedan')
My_second_car = Car('white', 'Mercedes-Benz', 'C300', '2016', 'sedan') 
My_third_car = Car('green', 'Lexux', 'RX 350', '2014', 'SUV')
My_fourth_car = Car('blue', 'BMW', 'M4 Convertible', '2022', 'convertible')
My_fifth_car = Car('matte black', 'Land Rover', 'Range Rover Sport', '2019', 'SUV')
 

print(My_first_car.car_color())
print(My_first_car.car_year())
print(My_first_car.car_body_type())