class Truck():

    def __init__(self, make, model, year: int, engine_liter: float, drivetrain):
        self.make = make
        self.model = model
        self.year = year
        self.engine_liter = engine_liter
        self.drivetrain = drivetrain

    def print_out_vehicle(self):
        return f"Make: {self.make}, Model: "
    
test_truck = Truck("Ford", "F250", 2012, 6.7, "4WD" )

print(test_truck.make)

class Specifications(Truck): 
    def __init__(self, mpg: int,trim_package, options, towing_capacity: int, payload: int, torque):
        # Either work grade or limited editiion its up to the user, and their wallet to decide what is right for them to 
        self.trim_package = trim_package
        self.options = options
        # towing capacity is what you can tow with your truck, towing capacity is in pounds
        # some heavy duty trucks, use dually tires with largerear diffrentials to add towing power.
        self.towing_capacity = towing_capacity
        # payload means basically what you can haul in your bed without attaching a trailer.
        self.payload = payload
        # torque is measured in ft/lbs and really makes a difference when hauling or in harsh conditions 
        # fun fact: Torque can be incresaed by tuning, deleting Deisel Exhaust Fluid (DEF)from your vehicle. Torque can also be increased by aspiration(how much air your engine takes in), otherwise, TURBO CHARGE IT
        self.torque = torque


class Tuning(Specifications, Truck):
    def __init__(self, )
    