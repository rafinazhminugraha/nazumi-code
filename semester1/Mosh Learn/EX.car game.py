print("Play Ur Car Now")

command_count_start = 0
command_count_stop = 0
command_first_stop = 0

while True:
    command = input("> ").lower()
    if command.lower() == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
              """)
    elif command == "start":
        command_count_start += 1
        command_first_stop += 1
        if command_count_stop > 0:
            command_count_stop -= 1
        if command_count_start == 2:
            command_count_start -= 1
            print("WDYM? Ur car already started!")
        elif command_count_start < 2:
            print("Car started... ready to go!")
    elif command == "stop":
        command_count_stop += 1
        if command_count_start > 0:
            command_count_start -= 1
        if command_count_stop == 2:
            command_count_stop -= 1
            print("Heyy ur car already stopped")
        elif command_count_start == 0 and command_first_stop == 0:
            command_count_stop -= 1
            print("Ur not even start ur car yet dumb dumb!")
        elif command_count_stop < 2:
            print("Car stopped")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")