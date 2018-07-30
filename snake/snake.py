# Implementation of classic game snake

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 200
HEIGHT = 200       
length = 1
snake = [[5, 10]]
   
# define event handlers
def new_game():
    global vel, snake, food, length, speed
    snake = [[0, 5]]
    speed = 10
    vel = [speed, 0]
    food = new_food()
    length = 1
    timer.start()
    
def new_food():
    return [random.randrange(WIDTH), random.randrange(HEIGHT)]

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def timer_handler():
    global vel, snake, food, length, speed
    head = snake[0]
    
    if dist(head, food) <= 10:
        food = new_food()
        length += 1
        speed = speed * 1.01
        
    head = [(head[0] + vel[0]) % WIDTH, (head[1] + vel[1]) % HEIGHT]
    
    tail = []
    
    for i in range(length - 1):
        tail.append(snake[i])
    
    tail.insert(0, head)
    
    snake = tail


def draw(canvas):
    global vel, snake, food, length, speed
    head = snake[0]
    tail = snake[1:]
    for body in tail:
        if dist(body, head) < 8:
            timer.stop()
    #canvas.draw_line(head, [head[0] + 15, head[1]], 15, 'White')
    canvas.draw_line(food, [food[0] + 10, food[1]], 10, 'White')
    for idx in range(0, length):
        canvas.draw_line(snake[idx], [snake[idx][0] + 10, snake[idx][1]], 10, 'White')
    
    
    
def keydown(key):
    """
    the key handlers to handle four direction keys
    """
    global vel, speed
    if key == simplegui.KEY_MAP["up"] and vel != [0, speed]:
        vel = [0, -speed]
    if key == simplegui.KEY_MAP["down"] and vel != [0, -speed]:
        vel = [0, speed]
    if key == simplegui.KEY_MAP["left"] and vel != [speed, 0]:
        vel = [-speed, 0]
    if key == simplegui.KEY_MAP["right"] and vel != [-speed, 0]:
        vel = [speed, 0]
    
    
# create frame
frame = simplegui.create_frame("Snake", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.add_button("Restart", new_game)

timer = simplegui.create_timer(100, timer_handler)


# start frame
new_game()
frame.start()
