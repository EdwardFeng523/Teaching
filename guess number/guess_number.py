import random
import simplegui

def generate():
    global randomNumber
    global time_remaining
    """
    randomly generates a number that is between 0 and num
    """
    randomNumber = random.randrange(100)
    time_remaining = 7


def guess(my_number):
    """
    This is a game that randomly generates a number then the
    player
    """
    global randomNumber
    global time_remaining
    if time_remaining == 0:
        print "You lost!"
    else:
        my_number = int(my_number)
        if my_number > randomNumber:
            print "Your guess is too high"
            print "Your have", time_remaining, "remaining guesses"
        if my_number < randomNumber:
            print "Your guess is too low"
            print "Your have", time_remaining, "remaining guesses"
        if my_number == randomNumber:
            print "Right guess!"
        time_remaining = time_remaining - 1
        
        

frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("New Game", generate)
frame.add_input("Enter guess", guess, 50)

frame.start()