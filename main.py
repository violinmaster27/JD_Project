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
        'room_description': 'Living room description',
        'room_actions': ['Action 1', 'Action 2', 'Action 3'],
        'action_results': ['Action 1 result', 'Action 2 result', 'Action 3 result']
    },
    {
        'name': 'kitchen',
        'room_description': 'Kitchen description',
        'room_actions': ['Action 1', 'Action 2', 'Action 3'],
        'action_results': ['Action 1 result', 'Action 2 result', 'Action 3 result']
    },
    {
        'name': 'bathroom',
        'room_description': 'Bathroom description',
        'room_actions': ['Action 1', 'Action 2', 'Action 3'],
        'action_results': ['Action 1 result', 'Action 2 result', 'Action 3 result']
    },
    {
        'name': 'bedroom',
        'room_description': 'Bedroom description',
        'room_actions': ['Action 1', 'Action 2', 'Action 3'],
        'action_results': ['Action 1 result', 'Action 2 result', 'Action 3 result']
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
                """)
            if room_input == 'L':
                change_room('living_room')
                break
            elif room_input == 'D':
                change_room('dining_room')
                break
            elif room_input == 'nvm':
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
                """)
            if room_input == 'K':
                change_room('kitchen')
                break
            elif room_input == 'BR':
                change_room('bedroom')
                break
            elif room_input == 'nvm':
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
                """)
            if room_input == 'K':
                change_room('kitchen')
                break
            elif room_input == 'BTH':
                change_room('bathroom')
                break
            elif room_input == 'nvm':
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
                """)
            if room_input == 'D':
                change_room('dining_room')
                break
            elif room_input == 'L':
                change_room('living_room')
                break
            elif room_input == 'BR':
                change_room('bedroom')
                break
            elif room_input == 'nvm':
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
                """)
            if room_input == 'L':
                change_room('living_room')
                break
            elif room_input == 'BR':
                change_room('bedroom')
                break
            elif room_input == 'nvm':
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
                """)
            if room_input == 'D':
                change_room('dining_room')
                break
            elif room_input == 'K':
                change_room('kitchen')
                break
            elif room_input == 'BTH':
                change_room('bathroom')
                break
            elif room_input == 'nvm':
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