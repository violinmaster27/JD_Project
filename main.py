# the main menu that user will see, they will choose which room to enter
USER_CHOICE = """
You have now entered the house. You must choose which room to enter.
    - '1' to enter the dining room
    - '2' to enter the living room
    - '3' to enter the kitchen
    - '4' to enter the bathroom
    - '5' to enter the bedroom
    - 'q' to quit

Enter your choice here: """

# empty list of room completed, this will fill up
# each time a room has been completed
rooms_completed = []


# each room will have its own function with challenges 'inside' each room

def dining_room():
    if '1' in rooms_completed:
        print("You have already completed the dining room.")
    else:
        print("You have entered the dining room.")
        room_input = input("Will you enter the kitchen or the bedroom? (3/5): ")

        if room_input == '3':
            kitchen()
        elif room_input == '5':
            bedroom()
        else:
            print("You cannot enter that room right now.")
            dining_room()

def living_room():
    if '2' in rooms_completed:
        print("You have already completed the living room.")
    else:
        print("You have entered the living room.")
        room_input = input("Will you enter the kitchen or the bathroom? (3/4): ")

        if room_input == '3':
            kitchen()
        elif room_input == '4':
            bathroom()
        else:
            print("You cannot enter that room right now.")
            living_room()

def kitchen():
    if '3' in rooms_completed:
        print("You have already completed the kitchen.")
    else:
        print("You have entered the kitchen.")
        room_input = input("Will you enter the dining room, living room, or the bedroom? (1/2/5): ")

        if room_input == '1':
            dining_room()
        elif room_input == '2':
            living_room()
        elif room_input == '5':
            bedroom()
        else:
            print("You cannot enter that room right now.")
            kitchen()

def bathroom():
    if '4' in rooms_completed:
        print("You have already completed the bathroom.")
    else:
        print("You have entered the bathroom.")
        room_input = input("Will you enter the living room or the bedroom? (2/5): ")

        if room_input == '2':
            living_room()
        elif room_input == '5':
            bedroom()
        else:
            print("You cannot enter that room right now.")
            bathroom()

def bedroom():
    if '5' in rooms_completed:
        print("You have already completed the bedroom.")
    else:
        print("You have entered the bedroom.")
        room_input = input("Will you enter the dining room, kitchen, or bathroom? (1/3/4): ")

        if room_input == '1':
            dining_room()
        elif room_input == '3':
            kitchen()
        elif room_input == '4':
            bathroom()
        else:
            print("You cannot enter that room right now.")
            bedroom()


def main():
    # dictionary of room options that will call the room function
    room_choices = {
        '1': dining_room,
        '2': living_room,
        '3': kitchen,
        '4': bathroom,
        '5': bedroom
    }

    user_input = input(USER_CHOICE)

    # if user does not choose to quit
    while user_input != 'q':
        # check if it's a valid room
        if user_input in ('1', '2', '3', '4', '5'):
            # call that room's function
            room_fuction = room_choices[user_input]
            room_fuction()
        else:
            print("Not a valid input. Please choose a valid room.")
            # prompt user for choice again
            user_input = input(USER_CHOICE)

    print("Quitting game.")
    quit()


main()
