class Specifications: 
    has_bed = True
    has_hitch = True
    def __init__(self, trim_package, horsepower: int, towing_capacity: int, payload: int,  torque: int):

        # these are public attributes 
        self.trim_package = trim_package
        self.horsepower = horsepower
        self.towing_capacity = towing_capacity
        self.payload = payload
        self.torque = torque

    def update_towing_capacity(self, towing_capacity):
        self.towing_capacity = towing_capacity
        return

    def update_horsepower(self, horsepower):
        self.horsepower = horsepower
        return 

    @classmethod
    def update_has_bed(cls, has_bed):
        cls.has_bed = has_bed
        if cls.has_bed == True:
            print("this truck has a bed!")
        else:
            print("this truck does not have a bed :(")
        return 

    @classmethod
    def update_has_hitch(cls, has_hitch):
        cls.has_hitch = has_hitch
        if cls.has_hitch == True:
            print("this truck has a hitch!")
        else:
            print("this truck does not have a hitch :(  very sad")
        return 


class Truck():

    is_heavy_duty = True
    is_dually = True

    def __init__(self, make, model, year: int, engine_liter: float, drivetrain):
        # I made these public 
        self.make = make
        self.model = model
        self.year = year
        self.engine_liter = engine_liter
        self.drivetrain = drivetrain
        self.specifications = []

    # two class methods
    @classmethod
    def update_is_dually(cls, is_dually, towing_capacity):
        towing_capacity += 14000
        if cls.is_heavy_duty == True:
            print("This Truck is heavy duty")
        else: 
            print("This Truck is not heavy duty.")
        return 


    @classmethod
    def update_is_heavy_duty(cls, is_heavy_duty):
        if cls.is_heavy_duty == True:
            print("Your Truck is ready to haul.")
        else: 
            print("Your truck is light duty, you shouldn't exceed 7,000lbs.")
        return 

    def add_spec(self, spec_obj):
        self.specifications.append(spec_obj)
        return 

    def display_spec(self):

        for spec in self.specifications:
            print("**** VEHICLE SPECIFICATIONS ****")
            print(f"Trim Package: {spec.trim_package}")
            print(f"Horsepower: {spec.horsepower}")
            print(f"Towing Capacity: {spec.towing_capacity}")
            print(f"Payload: {spec.payload}")
            print(f"Torque: {spec.torque}")
            print(f"has bed: {spec.has_bed}")
            print(f"has hitch: {spec.has_hitch}")
            print(f"is a dually: {Truck.is_dually}")
            print(f"Is a heavy duty model: {Truck.is_heavy_duty}")
         
        return "**** END VEHICLE SPECIFICATIONS ****"
                
        

# Here I make Tuning Inherit from Specifications. 
class Tuning(Specifications):

    has_cat_converter = False
    has_tune = False 

    def __init__(self, horsepower: int, torque: int ):
        self.horsepower = horsepower
        self.torque = torque
        
    def add_horsepower_torque_with_tune(self):
        self.horsepower += 50
        self.torque += 70
        return f"Updated hp is: {self.horsepower}hp. Updated Torque is {self.torque}lb ft."
        

    def add_cold_air_intake(self):
        self.horsepower += 20
        return f"Your Cold Air Intake added you gained {self.horsepower}hp."

    @classmethod
    def delete_catalytic_converter(cls, has_cat_converter):
        if has_cat_converter == True: 
            print("This truck has a catalytic converter!")
        else:
            print("This truck does not have a catalytic converter. roll some coal..")
        return 

    
    

# I also made Mod inherit from Specifications

class Mod(Specifications):

    has_lift_kit = False
    has_wheels = False

    def __init__(self, tint_percent: int, tailpipe_width: float):
       # these will be public attributes since we can change them some time
       self.tint_percent = tint_percent
       self.tailpipe_width = tailpipe_width

    # 6 inch tailpipe sounds the best and it isn't too loud.
    def add_better_tailpipe(self):
        self.tailpipe_diameter = 6.0
        return f"Your tailpipe width is {self.tailpipe_diameter}"

    def max_tint_windows(self):
        self.tint_percent = 5
        return f"Your window tint percent is {self.tint_percent}%."

 # made these class methods
    @classmethod
    def add_lift_kit(cls, has_lift_kit):
        cls.has_lift_kit = has_lift_kit
        if cls.has_lift_kit == True:
            print("Already gotcha a lift kit I see...")
        else: 
            print("Your truck has a lift kit.")
        return 

    @classmethod
    def add_wheels(cls, has_wheels):
        cls.has_wheels = has_wheels
        if cls.has_wheels == True:
            print("this truck already has wheels.")
        else:
            print("You now have American Forces wheels.")
        return 
    
    
########### TEST TRUCK AND SPECIFICATION CLASS ############

#self, trim_package, horsepower: int, towing_capacity: int, payload: int, torque: int
test_truck = Truck("GMC", "2500", 2011, 6.6, "4WD") 



#this is composition, adding specifications and appending them.
test_truck_spec = Specifications("Denali", 447, 15000, 3000, 730)

test_has_bed = Truck.update_is_heavy_duty(False)
test_is_heavy_duty = Truck.update_is_heavy_duty(False)
test_hitch = test_truck_spec.update_has_hitch(True)
test_bed = test_truck_spec.update_has_bed(True)

# here I will add the Specifications to the Truck() init
test_truck.add_spec(test_truck_spec)

# here I will print Out 

test_truck.display_spec()

########### END TEST TRUCK AND SPECIFICATION CLASS ############


######### TUNING CLASS TEST #########
#make an instance of the truck class pass in horsepower and torque
#tuner_truck = Tuning(397, 730)
#add our cold air intake will add HP
#add_cold_air_intake = tuner_truck.add_cold_air_intake()
# delete catalytic converter for better aspiration
#delete_cat_converter = tuner_truck.delete_catalytic_converter(False)
# we will print out the cold air intake message and cat converter message
#print(add_cold_air_intake)
#print(delete_cat_converter)


# now we will actually tune our vehicle!!
#truck_one = tuner_truck.add_horsepower_torque_with_tune()

#print(truck_one)

######### TUNING CLASS TEST END #########



######### MOD CLASS TEST #########

#mod_truck = Mod(60, 3.5)

#mod_lift_kit = mod_truck.add_lift_kit(False)
#mod_wheels = mod_truck.add_wheels(False)

#mod_tint = mod_truck.max_tint_windows()
#mod_tailpipe = mod_truck.add_better_tailpipe()

#print(mod_lift_kit)
#print(mod_wheels)
#print(mod_tailpipe)
#print(mod_tint)

######### MOD CLASS TEST END #########