'''
    AUTHOR : RAJAT AGRAWAL
'''
# importing  game specific modules
import pygame
import random
import numpy as np

#intialize pygame
x = pygame.init()

# load music file from directory
pygame.mixer.music.load("/home/rajat/Downloads/Game-Menu_Looping.mp3")

# colors used in the program
white = (255, 255, 255)
red = (255, 0, 0)
red2=(200,0,0)
black = (0, 0, 0)
orange=(153,153,153)
blue=(78,2,73)
green=(0,255,0)
green2=(34,177,76)

#set screen dimensions
screen_width = 1200
screen_height = 600

#set frames per second
fps=50
#load images used
img=pygame.image.load("/home/rajat/snakegame.bmp")

# creating window
gamewindow = pygame.display.set_mode((screen_width, screen_height))
#set game title
pygame.display.set_caption("The Interrupting Snake")
# update game window
pygame.display.update()

# set clock
clock = pygame.time.Clock()

# declare fonts to be used
font = pygame.font.SysFont("liberationserif", 30)

#create text surface object
def text_objects(text,color):
    # add text with font object along with its color
    textsurface=font.render(text,True,color)
    return textsurface,textsurface.get_rect()

#add text to button
def text_to_button(msg,color,button_x,button_y,bwidth,bheight):
    text_surf,textrect=text_objects(msg,color)
    textrect.center=((button_x+(bwidth/2)),button_y+(bheight/2))
    gamewindow.blit(text_surf,textrect)


#create buttons
def button(text,x,y,width,height,inactive_color,active_color,action):
    #get current positoion of mouse
    cur=pygame.mouse.get_pos()

    clicked=pygame.mouse.get_pressed()
    if x+width>cur[0]>x and y+height>cur[1]>y:
        #change color of button when mouse pointer is placed over it
        pygame.draw.rect(gamewindow,active_color,(x,y,width,height))
        #add on click event
        if clicked[0]==1 and action!=None:
            # quit or play game
            if action=="Quit":
                pygame.quit()
                quit()
            if action=="Play":
                gameloop()
    else:
        pygame.draw.rect(gamewindow, inactive_color, (x, y, width, height))
    text_to_button(text,black,x,y,width,height)

# stop music when gameover
def crashsound():
    pygame.mixer.music.stop()

#start screen of the game
def startscreen():
    intro=True
    while intro:
        #exit game when quit event is fired
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamewindow.fill(white)
        gamewindow.blit(img,(100,10))
        #messages on start screen
        text_screen("Welcome To The Interrupting Snake",green,100)
        text_screen("The Objective is to eat as many apples as you can",red,20)
        text_screen("But Wait! there is someone to interrupt you",green,-20)
        text_screen("Oh yes! it's the enemy snake beware `of it",red,-60)
        text_screen("Try to eat as many apples as you can without getting caught",green,-100)

        #display buttons
        button("Play",450,500,100,50,green2,green,"Play")
        button("Quit",650, 500, 100, 50,red2,red,"Quit")
        pygame.display.update()

# find closest point in a plane to a list of points int the same plane
def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    return np.argmin(dist_2)


#blit text onto the screen using text surface
def text_screen(text, color,y_displace):
    surface,textrect=text_objects(text,color)
    textrect.center=screen_width/2,screen_height/2-y_displace
    gamewindow.blit(surface,textrect)

#display score onto the screen
def scoredisp(text,color,x,y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text,(x,y))

#draw snake on the screen
def plot_snake(gamewindow,color,snk_lst,snake_size):
    for x,y in snk_lst:
        pygame.draw.circle(gamewindow,color,[x,y],snake_size-4,snake_size-4)

# create random food on the screen and check if the snake has eaten it
def eatfood(fx,fy,x,y,score,snk_length,init_velocity,c):
    global fps
    if abs(fx - x) < 10 and abs(fy - y) < 10: # compare x and y coordinates of snake-head and food
        if c==0:
            score += 10
        fps+=2
        # generate random food coordinates
        fx = random.randint(20, screen_width // 2)
        fy = random.randint(20, screen_height // 2)
        snk_length += 2
    return fx,fy,score,snk_length,init_velocity


# creating a game loop
def gameloop():
    # play music infinitely
    pygame.mixer.music.play(-1)
    # game specific variables
    exit_game = False
    game_over = False
    # initial postion of game objects
    food_x = random.randint(50, screen_width // 2)
    food_y = random.randint(50, screen_height // 2)
    snake_x = random.randint(100,500)
    snake_y = random.randint(200,500)
    comp_x=random.randint(400,600)
    comp_y=random.randint(300,600)
    # define computer velocities
    comp_velocity_x=0
    comp_velocity_y=0
    comp_velocity = 1
    #snake velocities
    velocity_x = 0
    velocity_y = 0
    #size of player snake
    snake_size = 10
    #size of computer snake
    comp_size=15
    #initial velocity of  player snake
    init_velocity = 3

    score=0

    #list to maintain snake coordinates
    snk_lst=[]
    comp_lst=[]
    # length of snakes
    comp_length=1
    snk_length=1

    flag=0
    fl=0
    fr=0
    # read current highscore from file
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over==True:
            global fps
            fps=50
            gamewindow.fill(white)
            #write updated highscore
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            # message if highscore is broken
            if score>=int(highscore):
                text_screen("Hurray New High-Score:"+str(highscore),blue,50)
            else:
                text_screen("OOPS GAME OVER",green,50)
            text_screen("PRESS SPACE TO PLAY AGAIN OR q TO QUIT",red,0)
            pygame.display.update()
            #define different actions for key presses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        exit_game=True
                    elif event.key==pygame.K_SPACE:
                        game_over=False
                        gameloop()
        else:
            #moving snake in different directions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        flag=1
                        if fl==0:
                            snake_x = snake_x + init_velocity
                            velocity_x = init_velocity
                            velocity_y = 0
                            fl=1
                            fr=0

                    elif event.key == pygame.K_LEFT:
                        flag=1
                        if fl==0:
                            snake_x = snake_x - init_velocity
                            velocity_x = -init_velocity
                            velocity_y = 0
                            fl=1
                            fr=0

                    elif event.key == pygame.K_DOWN:
                        flag=1
                        if fr==0:
                            snake_y = snake_y + init_velocity
                            velocity_y = init_velocity
                            velocity_x = 0
                            fl=0
                            fr=1

                    elif event.key == pygame.K_UP:
                        flag=1
                        if fr==0:
                            snake_y = snake_y - init_velocity
                            velocity_y = -init_velocity
                            velocity_x = 0
                            fr=1
                            fl=0
            # game over when snake hits the walls
            if snake_x<=0 or snake_x>=screen_width or snake_y<=0 or snake_y>=screen_height:
                crashsound()
                game_over=True
            #logic for computer snake chasing player snake
            if flag==1:
                indx = closest_node(comp_lst[0], snk_lst)
                node = snk_lst[indx]
                #if both snakes hit each other then game is over
                for i, j in snk_lst:
                    if abs(abs(comp_x) - abs(i)) < 5 and abs(abs(comp_y) - abs(j)) < 5:
                        crashsound()
                        game_over = True
                        break
                if node[0] < comp_x:
                    comp_x -= comp_velocity
                    comp_velocity_x = -comp_velocity
                    comp_velocity_y = 0
                if abs(abs(node[0]) - abs(comp_x)) < 10:
                    if node[1] > comp_y:
                        comp_y += comp_velocity
                        comp_velocity_x = 0
                        comp_velocity_y = comp_velocity
                    else:
                        comp_y -= comp_velocity
                        comp_velocity_x = 0
                        comp_velocity_y = -comp_velocity
                if node[0] > comp_x:
                    comp_x += comp_velocity
                    comp_velocity_x = comp_velocity
                    comp_velocity_y = 0

            snake_x += velocity_x
            snake_y += velocity_y
            comp_x+=comp_velocity_x
            comp_y+=comp_velocity_y
            # both snakes eating food
            food_x,food_y,score,snk_length,init_velocity = eatfood(food_x,food_y,snake_x,
                                                                 snake_y,score,snk_length,init_velocity,0)
            food_x, food_y, score, comp_length,init_velocity = eatfood(food_x, food_y, comp_x,
                                                                       comp_y, score, comp_length,init_velocity,1)
            #set background color to orange
            gamewindow.fill(orange)

            #draw red color walls
            pygame.draw.rect(gamewindow, red, [0, 0, screen_width, 4])
            pygame.draw.rect(gamewindow, red, [0, screen_height-4, screen_width, 4])
            pygame.draw.rect(gamewindow, red, [0, 0, 4, screen_height])
            pygame.draw.rect(gamewindow, red, [screen_width-4, 0, 4, screen_height + 2])

            # check if highscore is reached
            if score>int(highscore):
                highscore=score
            scoredisp("Score:"+str(score)+"   "+"High-Score:"+str(highscore), blue, 5, 5)
            pygame.draw.rect(gamewindow, green, [food_x, food_y, snake_size+2, snake_size+2])

            #list for storing snake head as it moves
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)

            if len(snk_lst) > snk_length:
                del snk_lst[0]
            #draw snake
            plot_snake(gamewindow, black, snk_lst, snake_size)

            # list for storing computer snake head as it moves
            comp_head=[]
            comp_head.append(comp_x)
            comp_head.append(comp_y)
            comp_lst.append(comp_head)
            if len(comp_lst)>comp_length:
                del comp_lst[0]
            # plot computer snake
            plot_snake(gamewindow,red,comp_lst,comp_size)
            pygame.display.update()
        #update clock
        clock.tick(fps)
    pygame.quit()
    quit()
startscreen()