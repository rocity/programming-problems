from random import randint


class Jellybean(object):
    """docstring for JellyBean"""
    def __init__(self, color, poisonous):
        self.color = color
        self.poisonous = poisonous
        super(Jellybean, self).__init__()

    def printProperties(self):
        print ("Color: %s" % self.color)
        print ("Poisonous: %s" % "Yes" if self.poisonous else "No")


class Instance(object):
    """docstring for Instance"""
    def __init__(self):
        super(Instance, self).__init__()

    def create(self):
        # create 3 jellybeans
        self.jellies = [
            Jellybean("Red", True),
            Jellybean("Blue", True),
            Jellybean("Green", True),
        ]

        return self

    def poison(self):
        # set a non-poisonous jelly
        poisoned = randint(0, 2)
        self.jellies[poisoned].poisonous = False

        return self

    def jellyStatus(self):
        for jelly in self.jellies:
            print (jelly.color)
            print (jelly.poisonous)
            print ("-----")


class Game(object):
    """docstring for Game"""
    def __init__(self, loops):
        self.loops = loops
        self.deaths = []
        self.choice = 0
        self.alwaysChange = True
        super(Game, self).__init__()

    def start(self):
        for i in range(1, self.loops):
            instance = Instance()

            # Reset choice every instance
            self.choice = 0

            # create jellybean set, then poison one
            instance.create()
            instance.poison()

            # user already has a choice (self.choice)
            print ("*** Instance #%s ***" % i)
            print ("--- Initial Choice ---")
            print (instance.jellies[self.choice].color)

            # pause to tell user that you will remove one jellybean from the stump
            jellylist = self.removeOnePoisoned(instance.jellies)
            print ("--- The executor removed a poisoned jellybean in your choices ---")

            # change choice to second jelly
            self.choice = 1

            # show player's choice
            print ("--- You changed your choice ---")
            print (jellylist[self.choice].color)

            # evaluate if user is dead
            if jellylist[self.choice].poisonous is True:
                # append to deaths list the index of this loop instance
                print ("You died.")
                self.deaths.append(i)
            else:
                print ("You live!")

        # end of for loop
        self.evaluateStats()

    def removeOnePoisoned(self, jellies):
        for index, jellybean in enumerate(jellies):
            if index != self.choice and jellybean.poisonous is True:
                # remove this jellybean since it is poisonous and it is not the choice
                del jellies[index]
        return jellies

    # solve stats
    def evaluateStats(self):
        deathRate = (len(self.deaths) / self.loops) * 100
        print ("=" * 10)
        print ("You died %s times out of %s instances." % (len(self.deaths), self.loops))
        print ("Your death rate is %s percent." % deathRate)
        print ("=" * 10)
