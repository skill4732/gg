from mammals import mammals



class horse(mammals):
    def __init__(self, viviparous, warm_blooded, wool, mammals, race, carry_gravity,):
        self.increased_endurance = race
        self.ruggledness = carry_gravity


    def __str__(self):
        return "viviparous: %s, warm_blooded: %s, wool: %s, mammals: %s, race: %s, carry_gravity: %s" % (self.viviparous, self.warm_blooded, self.wool, self.mammals, self.race, self.carry_gravity)