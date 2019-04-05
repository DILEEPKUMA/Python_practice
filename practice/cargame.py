car_action = ""
started=False

while car_action != "quit":
    car_action=input(">").lower()
    if car_action == 'start':
        if started:
            print("the car is already started ...")
        else:
            started=True
            print('the start....')
    elif car_action == 'stop':
        print ("the car is stop")
    elif car_action == 'help':
        print("""
        start-->the car is start
        stop-->the car is stop
        quit-->the car is quit
        """)
    elif car_action == "quit":
        break
    else:
        print("sorry...i dont understand")