class animals:

    def __init__(self, IQ, species, capabilities):
        self.IQ = IQ
        self.species = species
        self.capabilities = capabilities
        self.superiorIntelligence = []
        self.pinkify = []
        self.superpowers = []
        self.properties = []
        self.pinkiesco =[]
        self.capacities = ["the animal can speak", "the animal makes pinkish sounds"]

    def get_species(self):
        print(self.species+" , "+str(self.IQ)+" , "+self.capabilities)
    
    def get_transformation(self):
        if self.IQ == 17:
            addIQ1 = 100
            self.superiorIntelligence = self.IQ + addIQ1
            print(self.species+" has changed its intelligence to: " + str(self.superiorIntelligence))
        if self.IQ < 60:
            addIQ = 30
            self.superiorIntelligence = self.IQ + addIQ
            print(self.species + " has changed its intelligence to: " + str(self.superiorIntelligence))
        elif self.IQ > 60:
            addIQ2 = 20
            self.superiorIntelligence = self.IQ + addIQ2
            print(self.species+" has changed its intelligence to: "+str(self.superiorIntelligence))

    def get_pinkify(self):
        self.capabilities = self.capabilities.split(' ').pop(len(self.capabilities.split(' '))-1)
        print("successful pinkify!")
    
    def get_superpowers(self):
        if "Elephant" in self.species:
            superpower = "fly to kill enemies"
            self.superpowers = superpower
            print(self.species+" has changed its capabilities: "+self.capabilities+" to: "+self.superpowers)
        elif "Mouse" in self.species:
            if self.superiorIntelligence > 100:
                superpower = "speak"
                self.superpowers = superpower
                print(self.species+" has a superpower new: "+self.superpowers)
                return None
    
    def get_newProperties(self):
        if self.superiorIntelligence > 60:
            propertie = " the animal can speak"
            self.properties = propertie
            print(self.species+" is anthropomorphic and "+self.properties)
        elif self.superiorIntelligence < 60:
            propertie = " the animal makes pinkish sounds"
            pinkiesco = "do narf"
            self.properties = propertie
            self.pinkiesco = pinkiesco
            print(self.species+" is not so sane and "+self.properties)
            return None 

    def get_Pinkiesca(self):
        if "the animal makes pinkish sounds" in self.properties:
            if "do narf" in self.pinkiesco:
                print ("Pinkiesco is True")
                return None
    
    def get_report(self):
        if self.properties == self.capacities:
            print(self.species+" have among their capacities all the given capacities")
        else:
            print(self.species+" has not among their capacities all the given capacities")
        if "the animal can speak" in self.properties:
            print(str(self.superiorIntelligence)+" have any of the given capacities")
        elif "the animal makes pinkish sounds" in self.properties:
            print(str(self.superiorIntelligence)+" have any of the given capacities")
        else:
            print(self.species + " do not have any of the given capacities")



animal_1 = animals(120, "Elephant", "Thick skin to avoid insects")
animal_2 = animals(61, "Dragon", "Breathes fire to kill enemies")
animal_3 = animals(300, "Mouse", "adapt to changing surroundings and environments")
animal_4 = animals(18, "Butterfly", "Four wings to fly")
animal_experiment = animals(17, "Mouse", "destroy the world and make soulless plans")

print("part1: animals \n")        
animal_1.get_species()
animal_2.get_species()
animal_3.get_species()
animal_4.get_species()
print("\n")
print("part 2: transformation\n")   
animal_4.get_species()
animal_4.get_transformation()
animal_3.get_species()
animal_3.get_pinkify()
animal_1.get_species()
animal_1.get_superpowers()
print("\n")
print("part 3: transformation\n") 
animal_2.get_species()
animal_2.get_transformation()
animal_2.get_newProperties()
animal_4.get_species()
animal_4.get_transformation()
animal_4.get_newProperties()
animal_4.get_Pinkiesca()
print("\n")
print("part 4: experiment\n")
animal_experiment.get_species()
animal_experiment.get_pinkify()
animal_experiment.get_transformation()
animal_experiment.get_superpowers()
animal_experiment.get_newProperties()
print("\n")
print("part 5: report\n")
animal_1.get_species()
animal_1.get_transformation()
animal_1.get_newProperties()
animal_1.get_report()

