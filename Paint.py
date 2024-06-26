#import modules
import pygame
import button

#initialize pygame
pygame.init()

#define colors
white = (255, 255, 255)
gray = (175, 175, 175)
black = (0, 0, 0)
black2 = (50, 50, 50)
red = (255, 0, 0)
red2 = (200, 0, 0)
green = (76, 187, 23)
green2 = (26, 137, 0)
blue = (0, 0, 255)
blue2 = (0, 0, 200)
orange = (255, 140, 0)
orange2 = (200, 100, 0)
sienna = (109, 36, 14)
sienna2 = (80, 10, 0)

#define fonts
font = pygame.font.SysFont(None, 40)

#initialize game variables
screen_width = 1000
screen_height = 800
box_dim = 25
marker_max = 20
marker_min = 5

#initialize logic variables
clicked = False
color = black
marker_size = 10
tool = 1

#create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Paint')
icon = pygame.image.load("images/Bucket_tr.png").convert_alpha()
pygame.display.set_icon(icon)

#create rect objects
box = pygame.Rect(0, 0, box_dim, box_dim)

#load images
clear_img1 = pygame.image.load('images/clear_btn1.png').convert_alpha()
clear_img2 = pygame.image.load('images/clear_btn2.png').convert_alpha()
exit_img1 = pygame.image.load('images/exit_btn1.png').convert_alpha()
exit_img2 = pygame.image.load('images/exit_btn2.png').convert_alpha()
save_img1 = pygame.image.load('images/save_btn1.png').convert_alpha()
save_img2 = pygame.image.load('images/save_btn2.png').convert_alpha()
increase_img1 = pygame.image.load('images/increase_btn1.png').convert_alpha()
increase_img2 = pygame.image.load('images/increase_btn2.png').convert_alpha()
decrease_img1 = pygame.image.load('images/decrease_btn1.png').convert_alpha()
decrease_img2 = pygame.image.load('images/decrease_btn2.png').convert_alpha()
marker_box_img = pygame.image.load('images/marker_box.png').convert_alpha()
marker_box_img = pygame.transform.scale(marker_box_img, (53, 68))
brush_img1 = pygame.image.load('images/brush_btn1.png').convert_alpha()
brush_img2 = pygame.image.load('images/brush_btn2.png').convert_alpha()
eraser_img1 = pygame.image.load('images/eraser_btn1.png').convert_alpha()
eraser_img2 = pygame.image.load('images/eraser_btn2.png').convert_alpha()
black_img1 = pygame.Surface(box.size)
black_img1.fill(black)
black_img2 = pygame.Surface(box.size)
black_img2.fill(black2)
red_img1 = pygame.Surface(box.size)
red_img1.fill(red)
red_img2 = pygame.Surface(box.size)
red_img2.fill(red2)
green_img1 = pygame.Surface(box.size)
green_img1.fill(green)
green_img2 = pygame.Surface(box.size)
green_img2.fill(green2)
blue_img1 = pygame.Surface(box.size)
blue_img1.fill(blue)
blue_img2 = pygame.Surface(box.size)
blue_img2.fill(blue2)
orange_img1 = pygame.Surface(box.size)
orange_img1.fill(orange)
orange_img2 = pygame.Surface(box.size)
orange_img2.fill(orange2)
sienna_img1 = pygame.Surface(box.size)
sienna_img1.fill(sienna)
sienna_img2 = pygame.Surface(box.size)
sienna_img2.fill(sienna2)

#load cursors
marker_cursor = pygame.image.load('images/brush_tr.png').convert_alpha()
marker_cursor = pygame.transform.scale(marker_cursor, (24, 24))
eraser_cursor = pygame.image.load('images/eraser_tr.png').convert_alpha()
eraser_cursor = pygame.transform.scale(eraser_cursor, (24, 24))

#define functions
def clear_screen():
    screen.fill(white)

def Capture(display,pos,size): # (pygame Surface, String, tuple, tuple)

    #get image number
    number = 1
    
    #if file exists, read and update it
    try:
        with open("Paint_images/Paint_image_number.txt", 'r') as file:
            text = file.readlines()
            number = int(text[0])
        with open("Paint_images/Paint_image_number.txt", 'w') as file:
            file.write(str(number + 1))
            
    #if file does not exist, create it
    except FileNotFoundError:
        with open("Paint_images/Paint_image_number.txt", 'w') as file:
            file.write(str(number))

    name = f"Paint_images/image{number}.png"

    image = pygame.Surface(size)  # Create image surface
    image.blit(display,(0,0),(pos,size))  # Blit portion of the display to the image
    pygame.image.save(image,name)  # Save the image to the disk
    
    return number

#create button instances
clear_button = button.Button(10, 13, clear_img1, clear_img2, 0.4)
exit_button = button.Button(screen_width - exit_img1.get_width() * 0.4 - 10, 13, exit_img1, exit_img2, 0.4)
save_button = button.Button(10 + clear_img1.get_width() * 0.4 + 7, 13, save_img1, save_img2, 0.4)
increase_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + box_dim*2 + 10, 8, increase_img1, increase_img2, 0.5)
decrease_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + box_dim*2 + 10, 40, decrease_img1, decrease_img2, 0.5)
brush_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + box_dim*2 + 110, 13, brush_img1, brush_img2, 0.1)
eraser_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + box_dim*2 + 170, 13, eraser_img1, eraser_img2, 0.1)

#create button instances for colors
black_button = button.Button(102.8 + 92.8 + 15, 10, black_img1, black_img2, 1)
red_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7), 10, red_img1, red_img2, 1)
green_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7)*2, 10, green_img1, green_img2, 1)
blue_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7)*3, 10, blue_img1, blue_img2, 1)
orange_button = button.Button(102.8 + 92.8 + 15, 10 + (box_dim + 7), orange_img1, orange_img2, 1)
sienna_button = button.Button(102.8 + 92.8 + 15 + (box_dim + 7), 10 + (box_dim + 7), sienna_img1, sienna_img2, 1)

clear_screen()

#create a temporary pygame surface to save the screen before the cursor is printed
screen_tmp = pygame.Surface((screen_width, screen_height - 75))
screen_tmp.blit(screen,(0, 0),((0, 75),(screen_width, screen_height - 75)))

#hide mouse cursor and set to marker_cursor
pygame.mouse.set_visible(False)
cursor = marker_cursor

#game loop
run = True
while run:
    
    screen.blit(screen_tmp, (0, 75))
    
    #iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and clicked == False:
                pos_ini = pygame.mouse.get_pos()
                clicked = True
        if clicked:
            #check which tool is active
            if tool == 1: #marker
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, color, (pos[0], pos[1], marker_size, marker_size))
            if tool == 2: #eraser
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, white, (pos[0], pos[1], marker_size, marker_size))
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
            
    #draw toolbar
    pygame.draw.rect(screen, gray, (0, 0, screen_width, 75))
    pygame.draw.rect(screen, black, (0, 75, screen_width, 5))
            
    #draw buttons on toolbar
    if clear_button.draw(screen):
       clear_screen() 
       screen_tmp.fill(white)
    if exit_button.draw(screen):
        run = False
    if increase_button.draw(screen):
       marker_size += 1
       if marker_size > marker_max:
           marker_size = marker_max
    if decrease_button.draw(screen):
       marker_size -= 1
       if marker_size < marker_min:
           marker_size = marker_min
    if save_button.draw(screen):
        num = Capture(screen, (0, 75), (screen_width, screen_height - 75))
        print(f"Image saved as image{num}.png to Paint_images/image{num}.png")       
    if brush_button.draw(screen):
        tool = 1
        cursor = marker_cursor
    if eraser_button.draw(screen):
        tool = 2
        cursor = eraser_cursor
    
    #draw marker box on toolbar
    marker_size_txt = str(marker_size)
    marker_size_img = font.render(marker_size_txt, True, black)
    screen.blit(marker_box_img, (102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + box_dim*2 + 49, 4))
    if marker_size < 10:
        screen.blit(marker_size_img, (102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + box_dim*2 + 49 + 20, 3 + 32))
    else:
        screen.blit(marker_size_img, (102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + box_dim*2 + 49 + 11, 3 + 32))
    
    #draw color boxes on toolbar
    if black_button.draw(screen):
        color = black
    if red_button.draw(screen):
        color = red
    if green_button.draw(screen):
        color = green
    if blue_button.draw(screen):
        color = blue
    if orange_button.draw(screen):
        color = orange
    if sienna_button.draw(screen):
        color = sienna
        
    #show active color on toolbar
    pygame.draw.rect(screen, black2, (102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5, 13, box_dim*2, box_dim*2)) 
    pygame.draw.rect(screen, color, (102.8 + 92.8 + 15 + (box_dim + 7)*4 + 5 + 4, 13 + 4, box_dim*2 - 8, box_dim*2 - 8))    
        
    #save screen before printing cursor
    screen_tmp.blit(screen,(0, 0),((0, 75),(screen_width, screen_height - 75)))
    #draw cursor on screen
    pos = pygame.mouse.get_pos()
    if tool == 3:
        screen.blit(cursor, (pos[0] - 12, pos[1] - 12))
    else:
        screen.blit(cursor, (pos[0], pos[1] - 24))
    
    #update the display
    pygame.display.update()
    
#end pygame
pygame.quit()