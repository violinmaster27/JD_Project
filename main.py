import time
from Rooms import all_rooms

# ************ GAME STATE ************
current_room = 'front_door'
rooms_completed = []
is_hidden = False
has_keys = False
# will turn to true in the Study if user takes keys from there
has_escape_keys = False
has_knife = False
# this checks if user is already in a room, will limit the room location notice 
in_room = False
# this variable limits the room descriptions, will describe room only one time, unless user re-enters the room.
room_described = False 

# Any time actions
def prompt_action():
    USER_CHOICE = """
    Change rooms, look around the room, or give up. What do you do?
        - '1' to change rooms
        - '2' to look around the room
        - 'q' to give up (quit the game)

    Enter your choice here: """
    return USER_CHOICE

# need to break after calling change_room() or look_around() inside and loops or stuff will break, no pun intended
def change_room(room_name):
    time.sleep(1)
    eval(room_name + '()')

def hide():
    global is_hidden
    is_hidden = True

    leave_cover= input("Do you come out of hiding? (y/n)").upper()

    if leave_cover == "Y":
        is_hidden = False
        print("You leave the safety over your hiding place. :(((")
        return
    elif leave_cover == "N":
        print("You hide a bit longer...")
        time.sleep(3)
        hide()
    else:
        print("Not a valid answer. Try again.")
        hide()


def look_around(room_index):
    global room_described

    room = all_rooms[room_index]

    time.sleep(1)

    # will only print room description if user just entered the room
    if room_described == False:
        print(room.description)
        room_described = True 

    time.sleep(1)

    action_options = ""
    for index, action in enumerate(room.actions):
        if room.action_completed[index] == False:
            action_options = action_options + f'- {index + 1} to...' + action + '\n'

    if action_options != "":
        action_options = action_options + 'Enter your choice here: '
    else:
        change_room(current_room)

    # Type check user input
    while True:
        try:
            USER_CHOICE = int(input(action_options))
            break
        except ValueError:
            print('Please enter an integer value.')
    time.sleep(1)
    print(room.action_results[USER_CHOICE - 1])
    room.action_completed[USER_CHOICE - 1] = True

    time.sleep(1)

    # Here something happens, either nothing and it calls change_room again, or the player stays hidden, OR a specific special room method is called
    # If player picks certain action, activate its associated method and prompt the user again
    global is_hidden
    global has_keys
    global has_knife
    global has_escape_keys

    if room.name == 'front_door':
        if USER_CHOICE == 1:
            result = room.escape_the_house(has_escape_keys)
            if result == False:
                # let user choose this action again
                room.action_completed[0] = False
        if USER_CHOICE == 3:
            # let user choose closet hide action again
            hide()
            room.action_completed[2] = False

    if room.name == 'dining_room':
        if USER_CHOICE == 2:
            hide()
        if has_keys == False:
            # let user choose hide under table action again
            room.action_completed[1] = False

    if room.name == 'living_room':
        # player inspects safe
        if USER_CHOICE == 1:
            if has_keys == False:
                result = room.open_safe()
                if result:
                    has_keys = True
                    room.action_completed[0] = True 
                else:
                    # let player lift painting again since they don't have the key
                    room.action_completed[0] = False
            # keeping this else for lols. it's an easter egg
            else:
                print("I already opened this safe. Guess I'll take these pure diamonds too hehe yeaa boiiiiii.")

    if room.name == 'kitchen':
        # player inspects jar
        if USER_CHOICE == 1:
            room.inspect_jar()
        # player inspects knife
        if USER_CHOICE == 3:
            if has_knife == False:
                result = room.take_knife()
                if result:
                    has_knife = True
                else:
                    # let user choose this action again
                    room.action_completed[2] = False

    if room.name == 'bedroom':
        # player interacts with secret passageway
        if USER_CHOICE == 1:
            # always allow access to closet
            room.action_completed[0] = False
            result = room.go_up_passage(has_keys)
            if result:
                time.sleep(2)
                # player enters into library
                library()
        if USER_CHOICE == 2:
            room.open_book()

    if room.name == 'library':
        if USER_CHOICE == 2:
            # let user choose this action again
            room.action_completed[1] = False
            result = room.hide_in_shadows()
            if result:
                is_hidden = True

    if room.name == 'study':
        if USER_CHOICE == 1:
            room.read_letter()
        if USER_CHOICE == 2:
            if has_escape_keys == False:
                result = room.take_keys()
                if result:
                    has_escape_keys = True
        if USER_CHOICE == 3:
            hide()


    change_room(current_room)


def end_game():
    print("GAME OVER")
    quit()

# ************ ROOM FUNCTIONS ************

def front_door():
    global current_room
    global in_room
    global room_described
    current_room = "front_door"

    # will only print room location if user just entered the room, same goes with all the other rooms
    if in_room == False:
        print("You are at the front door. The stairway is blocked by debris.")
        time.sleep(2)
        in_room = True 

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the living room or the dining room? (L/D):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'L':
                in_room = False 
                room_described = False 
                change_room('living_room')
                break
            elif room_input == 'D':
                in_room = False
                room_described = False 
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
    global in_room 
    global room_described
    current_room = "dining_room"

    if in_room == False:
        print("You are in the dining room.")
        time.sleep(2)
        in_room = True 

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the kitchen, bedroom, or front door area? (K/BR/F):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'K':
                in_room = False
                room_described = False 
                change_room('kitchen')
                break
            elif room_input == 'BR':
                in_room = False 
                room_described = False 
                change_room('bedroom')
                break
            elif room_input == 'F':
                in_room = False 
                room_described = False 
                change_room('front_door')
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
    global in_room
    global room_described
    current_room = "living_room"

    if in_room == False:
        print("You are in the living room.")
        time.sleep(2)
        in_room = True

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the kitchen, bathroom, or front door area? (K/BTH/F):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'K':
                in_room = False
                room_described = False 
                change_room('kitchen')
                break
            elif room_input == 'BTH':
                in_room = False
                room_described = False 
                change_room('bathroom')
                break
            elif room_input == 'F':
                in_room = False
                room_described = False 
                change_room('front_door')
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
    global in_room 
    global room_described
    current_room = "kitchen"

    if in_room == False:
        print("You are in the kitchen.")
        time.sleep(2)
        in_room = True 

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the dining room, living room, or bedroom? (D/L/BR):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'D':
                in_room = False
                room_described = False 
                change_room('dining_room')
                break
            elif room_input == 'L':
                in_room = False
                room_described = False 
                change_room('living_room')
                break
            elif room_input == 'BR':
                in_room = False
                room_described = False 
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
    global in_room 
    global room_described
    current_room = "bathroom"

    if in_room == False:
        print("You are in the bathroom.")
        time.sleep(2)
        in_room = True 

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the living room or the bedroom? (L/BR):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'L':
                in_room = False
                room_described = False 
                change_room('living_room')
                break
            elif room_input == 'BR':
                in_room = False
                room_described = False 
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
    global in_room 
    global room_described
    current_room = "bedroom"

    if in_room == False:
        print("You are in the bedroom.")
        time.sleep(2)
        in_room = True 

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the dining room, kitchen, or bathroom? (D/K/BTH):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'D':
                in_room = False
                room_described = False 
                change_room('dining_room')
                break
            elif room_input == 'K':
                in_room = False
                room_described = False 
                change_room('kitchen')
                break
            elif room_input == 'BTH':
                in_room = False
                room_described = False 
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


def library():
    global current_room
    global in_room 
    global room_described
    current_room = "library"

    if in_room == False:
        print("You are in the library.")
        time.sleep(2)
        in_room = True 

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the study or go back to the bedroom? (S/BR):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'S':
                in_room = False
                room_described = False 
                change_room('study')
                break
            elif room_input == 'BR':
                in_room = False
                room_described = False 
                change_room('bedroom')
                break
            elif room_input == 'NVM':
                library()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(6)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())


def study():
    global current_room
    global in_room 
    global room_described
    current_room = "study"

    if in_room == False:
        print("You are in the study.")
        time.sleep(2)
        in_room = True 

    user_input = input(prompt_action())

    while True:
        if user_input == '1':
            room_input = input("""
                Will you enter the library? (y/n):
                I changed my mind. (nvm)
                """).upper()
            if room_input == 'Y':
                in_room = False
                room_described = False 
                change_room('library')
                break
            elif room_input == 'NVM' or room_input == 'N':
                study()
            else:
                print("Not a valid option. Choose again.")
                continue
        elif user_input == '2':
            look_around(7)
            break
        elif user_input == 'q':
            end_game()
        else:
            print("Not a valid input. Please choose a valid action.")
            user_input = input(prompt_action())


# ************ GAME START ************
def start_game():
    input("You have now entered the house. The front door locks behind you!"
          " The house is quiet but ominous. Find a way to get out, but don't "
          "take too long or else you might not make it out alive...")
    change_room(current_room)

start_game()
