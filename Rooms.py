import time
import random

global safe_number

def random_safe_code():
    global safe_number

    # use the randrange function from random library, make sure it'll always
    # be a 6 digit number
    safe_number = random.randrange(100000, 999999)

    return safe_number

random_safe_code()

class FrontDoor:
    name = 'front_door'
    description = 'The front door is a massive plank of dark oak, with a large golden handle.'
    actions = ['Try the front door.', 'Look up the stairs.', 'Hide inside the coat closet']
    action_results = ['The door is locked shut.', "Darkness...you hear faint footsteps on one of the upper floors. You're not alone.", 'You are hidden. You also find a spare tuxedo hanging in the closet, obviously the person who lived here liked to play football.']

    # only way to win the game so far, could be other ways if we want
    def escape_the_house(self, has_escape_keys):
        answer = input("Do you try to escape through the front door? (y/n)").upper()

        if answer == "Y":
            if has_escape_keys:
                print("You open the front door and escape this creepy house. YOU WIN!!")
                quit()
            else:
                print("You need the correct key to open this door. Go search the house, you may get lucky.")
        elif answer == "N":
            print("Well, at least you didn't waste your time.")
        else:
            print("Not a valid response. Try again.")
            self.escape_the_house(has_escape_keys)


class DiningRoom:
    global safe_number

    name = 'dining_room'
    description = """
                A long table sits at the center of the dining room, perfectly
                set with pristine china. A large chandelier floats above it,
                candlelight illuminating the small room with a warm glow.
                """
    actions = ['Sit at the table.', 'Hide under the table.', 'Inspect the chandelier.']
    action_results = ['The seat is warm. Suddenly you feel that someone is watching you.', f"The table cloth conseales you... You see a number carved into the underside of the table. '{safe_number}'", 'Whoever lives here needs to dust more often.']

    def specialInteraction(self):
        return 'If there is a special interaction it goes here.'


class LivingRoom:
    global safe_number

    name = 'living_room'
    description = """
                 Surprisingly, the living room seems well kept. Eveything is in
                 its right place. A large painting is hung on the wall. A
                 painting of some man, looks familiar from somewhere...
                 """

    actions = ['Lift the painting', 'Sit on the lounge sofa', 'Inspect the painting']
    action_results = ['You lift the painting to find some sort of safe behind it. If only you had the combination...', 'Creeek! Sitting on the sofa causes a loud noise.', 'You see initials on the bottom left of the painting: A.A. Probably the persons initials?']

    def open_safe(self):
        user_choice = input("Do you attempt to open the safe? (y/n) ").upper()

        if user_choice == 'Y':
            while True:
                try:
                    user_code = int(input("Enter the safe code: "))
                    break
                except ValueError:
                    print('Please enter an integer value.')

            if user_code == safe_number:
                print("You have opened the safe!! Inside you find a set of keys. These could be useful.")
                return True
            else:
                print("That is not the correct safe code. You could try again.\n")
                self.open_safe()

        elif user_choice == 'N':
            print("There's no way I can open it without the combination.")

        return False


class Kitchen:
    name = 'kitchen'
    description = """
                 You try to turn on the light but it doesn't work, maybe that's
                 for the better. Still, the kitchen has a strange odor to it,
                 and some dishes in the sink.
                 """

    actions = ['Check inside the fridge.', 'Look inside the cabinet.', 'Open the drawer next to the sink.']
    action_results = ['A putrid stench emits from the fridge, and you notice a cloudy jar on the top shelf.', 'Nothing special in here.', 'You find a sheathed knife lying in the drawer. It has some Asain writing on it.']

    @staticmethod
    def inspect_jar():
        user_choice = input("Do you wish to open the jar? (y/n) ").upper()

        if user_choice == 'Y':
            print("You open the jar to find some kind of egg inside. Who knows how long this has been here?")
        elif user_choice == 'N':
            print("Perhaps that was a wise choice. Stay safe.")

    @staticmethod
    def take_knife():
        user_choice = input("Do you take the knife? (y/n) ").upper()

        if user_choice == 'Y':
            print("The knife is pretty lightweight. This writing obviously means something, but I wonder what. You keep a hold of the knife just in case.")
            return True
        elif user_choice == 'N':
            print("Better leave it. Don't wanna hurt myself.")
            return False


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
    action_results = ["It's not a closet at all, but a secret passageway leading up somewhere...", 'Fitting, you find a copy of The Shining.', 'You see a figure pass by the door behind you...is it too late to leave?']

    def go_up_passage(self, has_keys):
        print("You go up the secret passageway. At the end is a door...but it's locked. You need a key to enter.")
        user_choice = input("Do you try to open the door? (y/n) ").upper()

        if user_choice == 'Y':
            if has_keys:
                # just had to add it here for dramatic effect
                time.sleep(2)
                print("You take a second to find the right key but once you do the door clicks open. You enter into the unknown.")
                return True
                # this will lead into the second floor of rooms
            else:
                print("You need a key to open this door. Find the keys and come back again.")
        elif user_choice == 'N':
            print("Be on your way, but don't waste any time!")

        return False

    @staticmethod
    def open_book():
        print("On the inside cover you see the writing: Property of A.A. Hmmm, this must be the owner of the house. If only I could remember who has those initials.")


class Library:
    name = 'library'
    description = """
                 After walking through the door, you see a welcome sight.
                 Shelves of books. This looks like a true treasure trove. An
                 armchair sits next to a fireplace with a fancy globe in the corner.
                 """
    actions = ['Inspect the large globe', 'Browse through the books', 'Inspect the fireplace']
    action_results = ['The globe opens up and inside are a bunch of pictures of violas.', 'Whoever lives here has good taste, now that I mention it, what happened to the steps I heard from up here? Maybe I should hide somwhere...', "This fireplace looks recently extinguished, I've really got to find a way out of this house..."]

    def hide_in_shadows(self):
        user_input = input("Do you hide in the shadows? (y/n)").upper()

        if user_input == "Y":
            print("You are hidden. You accidently knock down a book from the shelf...a thud breaks the silence.")
        elif user_input == "N":
            print("Feeling lucky today are we? Well, beware of danger.")
        else:
            print("Not a valid input. Try again.")
            self.hide_in_shadows()


class Study:
    name = 'study'
    description = """
                 The study is quite small but messy. There is a main desk and
                 there are lot's of loose papers lying around as well as an
                 important looking envelope. This room
                 should provide some useful information.
                 """

    actions = ['Open the envelope', 'Look through the desk drawer', 'Hide under the desk']
    action_results = ["Inside is a letter.", 'You find a another set of keys, maybe these will help you escape?', 'The house is quiet, but something tells you your not alone.']

    def read_letter(self):
        answer = input("Do you read the letter? (y/n)").upper()

        if answer == "Y":
            print("""
                Here is a clue for the user to figure out...
                Maybe tell them to look for an item somewhere in the room?
            """)
        elif answer == "N":
            print("You don't need help, you've got all you need inside your head.")
        else:
            print("Not a valid answer, try again.")
            self.read_letter()

    def take_keys(self):
        answer = input("Do you take the keys? (y/n)").upper()

        if answer == "Y":
            return True 
        elif answer == "N":
            print("You sure like to take risks, don't you??")
            return False 
        else:
            print("Not a valid answer. Try again.")
            self.take_keys()

front_door = FrontDoor()
dining_room = DiningRoom()
living_room = LivingRoom()
kitchen = Kitchen()
bathroom = Bathroom()
bedroom = Bedroom()
library = Library()
study = Study()

all_rooms = [front_door, dining_room, living_room, kitchen, bathroom, bedroom, library, study]
