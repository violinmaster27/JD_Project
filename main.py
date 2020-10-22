# ************ GAME STATE ************
# using the time.sleep() function will add some suspense to this game
# what do you think? i've incorporated it a bit so you can see what it's like
import time
from Rooms import all_rooms
# Set initial room
current_room = 'front_door'
rooms_completed = []
keys_attained = False
is_hidden = True

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
def change_room(room_name):
    time.sleep(1)
    eval(room_name + '()')

def look_around(room_index):
    room = all_rooms[room_index]

    time.sleep(1)

    print(room.description)

    action_options = ""
    for index, action in enumerate(room.actions):
        action_options = action_options + f'- {index + 1} to...' + action + '\n'
    # extra line to add this last line is kind of redundant
    action_options = action_options + 'Enter your choice here: '

    USER_CHOICE = input(action_options)
    time.sleep(1)
    print(room.action_results[int(USER_CHOICE) - 1])

    # Here something happens, either nothing and it calls change_room, or the player stays hidden, OR special room method is called
    # If player picks certain action, activate its associated method and prompt the user again

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
    time.sleep(2)

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the living room or the dining room? (L/D):
                I changed my mind. (NVM)
                """)
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
    time.sleep(1)

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the kitchen or the bedroom? (K/BR):
                I changed my mind. (NVM)
                """)
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
    time.sleep(1)

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the kitchen or the bathroom? (K/BTH):
                I changed my mind. (NVM)
                """)
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
    time.sleep(1)

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the dining room, living room, or bedroom? (D/L/BR):
                I changed my mind. (NVM)
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
    time.sleep(1)

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the living room or the bedroom? (L/BR):
                I changed my mind. (NVM)
                """)
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
    time.sleep(1)

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the dining room, kitchen, or bathroom? (D/K/BTH):
                I changed my mind. (NVM)
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
    print("You have now entered the house. The front door locks behind you! The house is quiet but ominous.")
    time.sleep(2)
    change_room(current_room)

start_game()
