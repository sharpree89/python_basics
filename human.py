class Human(object):
    def __init__(self, clan=None):
        print "New Human!"
        self.clan = clan
        self.health = 100
        self.strength = 3
        self.intelligence = 3
        self.stealth = 3
    def taunt(self):
        print "you want a piece of me?"
    def stats(self):
        print "Clan: {}; Health: {}; Strength: {}; Intelligence: {}; Stealth: {}".format(self.clan, self.health, self.strength, self.intelligence, self.stealth)

preeya = Human("Coding Dojo")
preeya.stats()
preeya.taunt()
