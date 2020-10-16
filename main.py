# ************ GAME STATE ************
# Set initial room
current_room = "front_door"
rooms_completed = []
all_rooms = [
    {
        'name': 'front_door',
        'room_description': 'The front door is a massive plank of dark oak, with a large golden handle.',
        'room_actions': ['Try the front door.', 'Look up the stairs.', 'Hide inside the coat closet'],
        'action_results': ['The door is locked shut. It will not budge.', 'Darkness...you hear faint footsteps on one of the upper floors.', 'You are hidden. You also find a spare tuxedo hanging in the closet, obviously the person who lived here liked to play football.']
    },
    {
        'name': 'dining_room',
        'room_description': 'A long table sits at the center of the dining room, perfectly set with pristine china. A large chandelier floats above it, candlelight illuminating the small room with a warm glow.',
        'room_actions': ['Sit at the table.', 'Hide under the table.', 'Inspect the chandelier.'],
        'action_results': ['The seat is warm.', 'The table cloth conseales you... You find a message carved on the underside of the table.', 'It is rusty.']
    },
    {
        'name': 'living_room',
        'room_description': 'Surprisingly, the living room seems well kept. Eveything is in its right place. A large painting is hung on the wall. A painting of some man, looks familiar from somewhere...',
        'room_actions': ['Lift the painting', 'Sit on the lounge sofa', 'Inspect the painting'],
        'action_results': ['You lift the painting to find some sort of safe behind it. If only you had the combination...', 'Creeek! Sitting on the sofa causes a loud noise.', 'You see initials on the bottom left of the painting: A.A. Probably the persons initials?']
    },
    {
        'name': 'kitchen',
        'room_description': "You try to turn on the light but it doesn't work, maybe that's for the better. Still, the kitchen has a strange odor to it, and some dishes in the sink.",
        'room_actions': ['Check inside the fridge.', 'Look inside the cabinet.', 'Open the drawer next to the sink.'],
        'action_results': ['A putrid stench emits from the fridge, and you notice a cloudy jar on the top shelf.', 'Nothing special in here.', 'You find a sheathed knife lying in the drawer. It has some Asain writing on it.']
    },
    {
        'name': 'bathroom',
        'room_description': 'The bathroom is small. Not a pleasant smell at all, and the light flickers for a while before fully turning on.',
        'room_actions': ['Flush the toilet.', 'Open the medicine cabinet.', 'Pull back the shower curtain.'],
        'action_results': ['It seems broken...I guess the smell is staying.', 'A lot of painkillers...and fungicide, fungus???', 'It is as you feared, a small pool of blood remains in the tub.']
    },
    {
        'name': 'bedroom',
        'room_description': 'A very simple looking bedroom. Signs of use appear throughout the room. But where is the resident?',
        'room_actions': ['Look in the Closet', 'Search the Nightstand', 'Look in the mirror'],
        'action_results': ["It's not a closet at all, but a secret passageway leading up somehwere...", 'Fitting, you find a copy of The Shining.', 'You see a figure pass by the door behind you...is it too late to leave?']
    }
]

# Any time actions
def prompt_action():
    USER_CHOICE = """
    Change rooms, look around, or give up. What do you do?
        - '1' to change rooms
        - '2' to look around
        - 'q' to give up (quit the game)

    Enter your choice here: """
    return USER_CHOICE

# need to break after calling change_room() or look_around() inside and loops or stuff will break, no pun intended
def change_room(room):
    eval(room + '()')

def look_around(room_index):
    room = all_rooms[room_index]

    print(room.get('room_description'))

    action_options = ""
    for index, action in enumerate(room.get('room_actions')):
        action_options = action_options + f'- {index + 1} to...' + action + '\n'
    # extra line to add this last line is kind of redundant
    action_options = action_options + 'Enter your choice here: '

    USER_CHOICE = input(action_options)
    print(room.get('action_results')[int(USER_CHOICE) - 1])

    # call room function again to continue, obviously this shouldnt happen if the player is hidden but we'll deal with that soon
    change_room(current_room)


def end_game():
    print("GAME OVER")
    quit()

# ************ ROOM FUNCTIONS ************

def front_door():
    global current_room
    current_room = "front_door"

    print("You are at the front door. The stairway is blocked by debris.")

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the living room or the dining room? (L/D):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'L':
                change_room('living_room')
                break
            elif room_input == 'D':
                change_room('dining_room')
                break
            elif room_input == 'NVM':
                front_door()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(0)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())

def dining_room():
    global current_room
    current_room = "dining_room"

    print("You are in the dining room.")

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the kitchen or the bedroom? (K/BR):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'K':
                change_room('kitchen')
                break
            elif room_input == 'BR':
                change_room('bedroom')
                break
            elif room_input == 'NVM':
                dining_room()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(1)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())


def living_room():
    global current_room
    current_room = "living_room"

    print("You are in the living room.")

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the kitchen or the bathroom? (K/BTH):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'K':
                change_room('kitchen')
                break
            elif room_input == 'BTH':
                change_room('bathroom')
                break
            elif room_input == 'NVM':
                living_room()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(2)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())


def kitchen():
    global current_room
    current_room = "kitchen"

    print("You are in the kitchen.")

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the dining room, living room, or bedroom? (D/L/BR):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'D':
                change_room('dining_room')
                break
            elif room_input == 'L':
                change_room('living_room')
                break
            elif room_input == 'BR':
                change_room('bedroom')
                break
            elif room_input == 'NVM':
                kitchen()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(3)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())


def bathroom():
    global current_room
    current_room = "bathroom"

    print("You are in the bathroom.")

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the living room or the bedroom? (L/BR):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'L':
                change_room('living_room')
                break
            elif room_input == 'BR':
                change_room('bedroom')
                break
            elif room_input == 'NVM':
                bathroom()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(4)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())


def bedroom():
    global current_room
    current_room = "bedroom"

    print("You are in the bedroom.")

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the dining room, kitchen, or bathroom? (D/K/BTH):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'D':
                change_room('dining_room')
                break
            elif room_input == 'K':
                change_room('kitchen')
                break
            elif room_input == 'BTH':
                change_room('bathroom')
                break
            elif room_input == 'NVM':
                bedroom()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(5)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())


# ************ GAME START ************
def start_game():
    print("You have now entered the house. The front door locks behind you! The house is silent but ominous.")
    change_room(current_room)

start_game()
