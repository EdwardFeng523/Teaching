import random
import simplegui

allwords = [
    'runs', 'experience', 'comments', 'freedom', 'permit', 'honks', 'pins', 'texts', 'grant', 'fathers',
 'raincoat', 'reactance', 'room', 'relocation', 'rough','expansion', 'exercise', 'clay', 'farads', 
 'path', 'scenes', 'lifetime', 'drinks', 'railways', 'vacuum', 'country', 'code', 'houston', 'swim', 'reserve',
 'walk', 'secret', 'install', 'engineer', 'beautiful', 'president', 'laugh', 'pretty', 'sincere', 'honest', 'abnormal',
 'vector', 'matrix', 'school', 'documentation']

display = ""
tries = ""
triesdraw = ""
reminder = ""

def start():
    """
    Randomly choose some word and make global variables for future use.
    """
    global word
    global display
    global tries
    global triesdraw
    word = random.choice(allwords)
    tries = len(word)
    triesdraw = "Remaining tries = " + str(tries)
    display = []
    for idx in range(tries):
        display.append("_")
    

def hangman(guess):
    """
    take our guess and do the corresponding response
    """
    global word
    global display
    global tries
    global triesdraw
    global message
    global reminder
    if tries == 0:
        message = "You lose, the word is " + word
        reminder = "Start a new game!"
    else:
        if guess not in word:
            tries = tries - 1
            if tries == 0:
                message = "You lose, the word is " + word
            triesdraw = "Remaining tries = " + str(tries)
        for idx in range(len(word)):
            if word[idx] == guess:
                display[idx] = guess
        count = 0
        for element in display:
            if element == "_":
                count = count + 1
        if count == 0:
            message = "You win!"
            
import simplegui

message = "Welcome!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [15,102], 20, "White")
    canvas.draw_text(reminder, [15,122], 20, "White")
    canvas.draw_text(str(display), [20, 140], 20, "White")
    canvas.draw_text(str(triesdraw), [20, 160], 20, "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 400)
frame.add_button("New Game", start)
frame.add_input("Guess", hangman, 50)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


    