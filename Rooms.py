class FrontDoor:
    name = 'dining_room'
    description = 'The front door is a massive plank of dark oak, with a large golden handle.'
    actions = ['Try the front door.', 'Look up the stairs.', 'Hide inside the coat closet']
    action_results = ['The door is locked shut. It will not budge.', "Darkness...you hear faint footsteps on one of the upper floors. You're not alone.", 'You are hidden. You also find a spare tuxedo hanging in the closet, obviously the person who lived here liked to play football.']

    def specialInteraction(self):
        return 'If there is a special interaction it goes here.'


class DiningRoom:
    name = 'dining_room'
    description = 'A long table sits at the center of the dining room, perfectly set with pristine china. A large chandelier floats above it, candlelight illuminating the small room with a warm glow.'
    actions = ['Sit at the table.', 'Hide under the table.', 'Inspect the chandelier.']
    action_results = ['The seat is warm. Suddenly you feel that someone is watching you.', "The table cloth conseales you... You see a number carved into the underside of the table. '5-1-1-4-3-3'", 'Whoever lives here needs to dust more often.']

    def specialInteraction(self):
        return 'If there is a special interaction it goes here.'


class LivingRoom:
    name = 'living_room'
    description = 'Surprisingly, the living room seems well kept. Eveything is in its right place. A large painting is hung on the wall. A painting of some man, looks familiar from somewhere...'
    actions = ['Lift the painting', 'Sit on the lounge sofa', 'Inspect the painting']
    action_results = ['You lift the painting to find some sort of safe behind it. If only you had the combination...', 'Creeek! Sitting on the sofa causes a loud noise.', 'You see initials on the bottom left of the painting: A.A. Probably the persons initials?']

    def open_safe(self):
        safe_code = int(input("Enter the safe code: "))

        if safe_code == 511433:
            print("You have opened the safe!! Inside you find a set of keys. These could be useful.")
            return True
        else:
            print("That is not the correct safe code.\n")
            user_choice = input("Do you wish to try again? (y/n)").upper()

            if user_choice == "Y":
                self.open_safe()
            elif user_choice == "N":
                print("Sounds good.")

        return False


class Kitchen:
    name = 'kitchen'
    description = "You try to turn on the light but it doesn't work, maybe that's for the better. Still, the kitchen has a strange odor to it, and some dishes in the sink."
    actions = ['Check inside the fridge.', 'Look inside the cabinet.', 'Open the drawer next to the sink.']
    action_results = ['A putrid stench emits from the fridge, and you notice a cloudy jar on the top shelf.', 'Nothing special in here.', 'You find a sheathed knife lying in the drawer. It has some Asain writing on it.']

    def take_knife(self):
        print("The knife is pretty lightweight. This writing obviously means something, but I wonder what. You keep a hold of the knife just in case.")

    def inspect_jar(self):
        user_choice = input("Do you wish to open the jar? (y/n)")

        if user_choice == 'y':
            print("You open the jar to find some kind of egg inside. Who knows how long this has been here?")
        elif user_choice == 'n':
            print("Perhaps that was a wise choice. Stay safe.")


class Bathroom:
    name = 'bathroom'
    description = 'The bathroom is small. Not a pleasant smell at all, and the light flickers for a while before fully turning on.'
    actions = ['Flush the toilet.', 'Open the medicine cabinet.', 'Pull back the shower curtain.']
    action_results = ['It seems broken...I guess the smell is staying.', 'A lot of painkillers...and fungicide, fungus???', 'It is as you feared, a small pool of blood remains in the tub.']

    def specialInteraction(self):
        return 'If there is a special interaction it goes here.'


class Bedroom:
    name = 'bedroom'
    description = 'A very simple looking bedroom. Signs of use appear throughout the room. But where is the resident?'
    actions = ['Look in the Closet', 'Search the Nightstand', 'Look in the mirror']
    action_results = ["It's not a closet at all, but a secret passageway leading up somehwere...", 'Fitting, you find a copy of The Shining.', 'You see a figure pass by the door behind you...is it too late to leave?']

    def go_up_passage(self, keys_attained):
        print("You go up the secret passageway. At the end is a door...but it's locked. You need a key to enter.")
        user_choice = input("Do you try to open the door? (y/n)").lower()

        if user_choice == 'y':
            if keys_attained:
                print("You open the door and enter into the unknown.")
                # this will lead into the second floor of rooms
            else:
                print("You need a key to open this door. Find the keys and come back again.")
        elif user_choice == 'n':
            print("Be on your way, but don't waste any time!")


    def open_book(self):
        print("On the inside cover you see the writing: Property of A.A. Hmmm, this must be the owner of the house. If only I could remember who has those initials.")


front_door = FrontDoor()
dining_room = DiningRoom()
living_room = LivingRoom()
kitchen = Kitchen()
bathroom = Bathroom()
bedroom = Bedroom()

all_rooms = [front_door, dining_room, living_room, kitchen, bathroom, bedroom]
