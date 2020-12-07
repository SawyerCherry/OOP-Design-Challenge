# Second Class Is called Specifications and It takes in truck as a parameter. This means it will inherit from the Truck Class. 

class Specifications(): 

    has_bed = True
    has_hitch = True

    def __init__(self, trim_package, horsepower: int, towing_capacity: int, payload: int, torque: int):
        # Either work grade or limited editiion its up to the user, and their wallet to decide what is right for them to 

        self.trim_package = trim_package
        
        self.horsepower = horsepower

        # towing capacity is what you can tow with your truck, towing capacity is in pounds
        # some heavy duty trucks, use dually tires with largerear diffrentials to add towing power.

        self.towing_capacity = towing_capacity
        # payload means basically what you can haul in your bed without attaching a trailer.
        self.payload = payload
        # torque is measured in ft/lbs and really makes a difference when hauling or in harsh conditions 
        # fun fact: Torque can be incresaed by tuning, deleting Deisel Exhaust Fluid (DEF)from your vehicle. Torque can also be increased by aspiration(how much air your engine takes in), otherwise, TURBO CHARGE IT
        self.torque = torque

    def update_towing_capacity(self, towing_capacity):
        self.towing_capacity = towing_capacity

    def update_horsepower(self, horsepower):
        self.horsepower = horsepower

    @classmethod
    def update_has_bed(cls, has_bed):
        cls.has_bed = has_bed
        if cls.has_bed == True:
            print("this truck has a bed!")
        else:
            print("this truck does not have a bed :(")

    @classmethod
    def update_has_hitch(cls, has_hitch):
        cls.has_hitch = has_hitch
        if cls.has_hitch == True:
            print("this truck has a hitch!")
        else:
            print("this truck does not have a hitch :(  very sad")

class Truck():

    def __init__(self, make, model, year: int, engine_liter: float, drivetrain):
        self.make = make
        self.model = model
        self.year = year
        self.engine_liter = engine_liter
        self.drivetrain = drivetrain
        self.specifications = None

    def print_out_vehicle(self):
        return f"Make: {self.make}, Model: "


    def add_spec(self, spec_obj):
        self.specifications = spec_obj
        
    
test_truck = Truck("Ford", "F250", 2012, 6.7, "4WD" )
test_truck_spec = Specifications("Denali", 447, 15000, 3000, 730)
test_truck.add_spec(test_truck_spec)

print(test_truck.specifications.trim_package)



# test_spec = ######(18, "Limited", )

class Tuning(Specifications):
    
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def delete_catalytic_converter(self):
        return "you no longer have a catalytic converter"

    def add_horsepower_with_tune(self, horsepower):
        horsepower += 50
        return f"your updated hp is: {horsepower}"

tuner_truck = Tuning(447)
truck_one = Tuning.add_horsepower_with_tune()

print(truck_one)

class Mod(Specifications):

    has_lift_kit = False
    has_wheels = False

    def __init__(self, tint_percent: int, tailpipe_width: float):
       
       self.tint_percent = tint_percent
       self.tailpipe_width = tailpipe_width


    @classmethod
    def add_lift_kit(cls, has_lift_kit):
        cls.has_lift_kit = has_lift_kit
        if cls.has_lift_kit == True:
            print("Already gotcha a lift kit I see...")
        else: 
            has_lift_kit = True
            print("Your truck has a lift kit.")

    @classmethod
    def add_wheels(cls, has_wheels):
        cls.has_wheels = has_wheels
        if cls.has_wheels == True:
            print("this truck already has wheels.")
        else:
            cls.has_wheels = True
            print("You now have American Forces wheels.")
    
    

mod = Mod.add_lift_kit(False)
mod_two = Mod.add_wheels(False)

print(mod)
print(mod_two)