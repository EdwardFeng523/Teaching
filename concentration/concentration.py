# Concentration

import simplegui
import random

# set globals
deck = range(8)
deck_a = range(8)
deck.extend(deck_a)
exposed = []
turns = 0
a = 0
b = 0

# helper function to initialize globals
def new_game():
    global state, deck, turns, exposed
    random.shuffle(deck)
    state = 0  
    turns = 0
    exposed = []
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    global state, turns, a, b
    if not pos[0] // 50 in exposed:
        if state == 0:
            state = 1
            turns += 1
            a = pos[0] // 50
            exposed.append(a)
        elif state == 1:
            state = 2
            b = pos[0] // 50
            exposed.append(b)
        else:
            if deck[a] == deck[b]:
                a = pos[0] // 50
                exposed.append(a)
            elif deck[a] != deck[b]:
                exposed.remove(a)
                exposed.remove(b)
                a = pos[0] // 50
                exposed.append(a)
            state = 1
            turns += 1
        
    label.set_text("Turns = " + str(turns))
    
        
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for idx in range(len(deck)):
        if idx in exposed:
            canvas.draw_text(str(deck[idx]), [10 + 50 * idx, 65], 50, "White")
        else:
            canvas.draw_polygon([[50 * idx, 0], [50 + 50 * idx, 0], 
                                 [50 + 50 * idx, 100], [50 * idx, 100]], 
                                1, 'Orange', 'Green')
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric