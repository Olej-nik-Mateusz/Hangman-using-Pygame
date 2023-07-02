import pygame
import os
import string
import math
import rndWord



# setup display
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# colors pallette
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (200, 0, 200)

# fonts
alphabet = string.ascii_uppercase # ASCII characters for letters on buttons
LETTER_FONT = pygame.font.SysFont('comicsans', 30) 
WORD_FONT = pygame.font.SysFont('comicsans', 40) 
TITLE_FONT = pygame.font.SysFont("comicsans", 60)

# game variables
hangman_status = 0
guessWord = rndWord.rndGuessWord(rndWord.getList())
inWordList = []

# button variables
RADIUS = 20
GAP = 15
letters = []
startX = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) 
startY = 500

# get button positions
for i in range(26):
    x = startX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = startY + ((i // 13) * (GAP + RADIUS *2))
    letters.append([x, y, alphabet[0+i], True])


def draw():
    win.fill(WHITE)     # fill window (white) 
    
    # title draw
    text = TITLE_FONT.render("HANGMAN GAME",1, BLACK )
    win.blit(text, (round(WIDTH/2 - text.get_width()/2), 50))

    # draw word
    printWord = [letter if letter in inWordList else "_" for letter in guessWord]
    printed = ' '.join(printWord)
    text = WORD_FONT.render(printed, 1, BLACK)
    win.blit(text, (round(WIDTH/2 - text.get_width()/2), 350))

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter 
        if visible: 
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)   
            text = LETTER_FONT.render(ltr, 1, BLACK)    
            win.blit(text, ((x-text.get_width()/2), y-text.get_height()/2)) # draw letters in buttons

    win.blit(images[hangman_status], (80, 170)) # draw images
    pygame.display.update()    

# load images
images = []
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
    
    
# setup game run loop
FPS=60
clock = pygame.time.Clock()
run=True


# is letter in word
def inWord(letter, inWordList):
    
    if letter[2] in guessWord:
      inWordList.append(letter[2])
    

while run:
    clock.tick(FPS)
    draw()
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:       # QUIT game event 
            run = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:        # mouse "click" event
            mouseX, mouseY = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dist =  math.sqrt((x- mouseX)**2 + (y - mouseY)**2)
                    if dist < RADIUS:
                        letter[3] = False
                        print(letter[2])
                        inWord(letter, inWordList)
                        if ltr not in guessWord:
                            hangman_status += 1

    won= True
    for letter in guessWord:
        if letter not in inWordList:
            won=False
            break
    if won:
        win.fill(WHITE)
        text = WORD_FONT.render(f"You WON ! ", 1, PURPLE)
        win.blit(text, ((WIDTH - text.get_width())/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)
        break
        
    if hangman_status == 6:
        win.fill(WHITE)
        text = WORD_FONT.render(f"You LOST !", 1, PURPLE)
        text2 = WORD_FONT.render(f"It was {guessWord}", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()-50/2))
        win.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 - text2.get_height()+50/2))
        pygame.display.update()
        pygame.time.delay(4000)
        break
                

pygame.quit()


