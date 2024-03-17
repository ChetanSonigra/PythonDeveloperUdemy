import pygame, random,math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption('Space Invasion')
icon = pygame.image.load('python1/Day10/ufo.png')
pygame.display.set_icon(icon)
background_img = pygame.image.load('python1/Day10/Background.png')

# Add music
mixer.music.load('python1/Day10/background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Players variable
player_img = pygame.image.load('python1/Day10/rocket.png')
player_x = 368  # 400 - (64/2)
player_y = 536 # 600 - 64
player_x_change = 0
player_y_change = 0 

# enemy variable
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemy = 10

for e in range(number_of_enemy):

    enemy_img.append(pygame.image.load('python1/Day10/enemy.png'))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(0,250))
    enemy_x_change.append(4)
    enemy_y_change.append(70)

# bullet variable
bullet_img = pygame.image.load('python1/Day10/bullet.png')
bullet_x = 0
bullet_y = 536
bullet_x_change = 0
bullet_y_change = 10
bullet_visible = False

# score
score = 0
my_font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# end of game text
end_font = pygame.font.Font('freesansbold.ttf', 50)

# 
def final_text():
    my_final_font = end_font.render('GAME OVER', True, (255,0,0))
    screen.blit(my_final_font, (250,250))
    
# show score function
def show_score(x,y):
    text = my_font.render(f'Score: {score}', True, (255,255,255))
    screen.blit(text, (x,y))
    
# Player function
def player(x,y):
    screen.blit(player_img, (x, y))

# Enemy function
def enemy(x,y,enem_index):
    screen.blit(enemy_img[enem_index], (x, y))

# bullet function
def shoot_bullet(x,y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img, (x+16,y))
    
# determine collition
def there_is_collition(x1,y1,x2,y2):
    distance = math.sqrt((math.pow(x1-x2,2) + math.pow(y1-y2, 2)))
    if distance < 27:
        return True
    return False

# Game Loop
is_running = True
while is_running:
    # RGB
    # screen.fill((205,144,228))
    # Background image
    screen.blit(background_img, (0,0))
    
    # event iteration
    for event in pygame.event.get():
        # closing event
        if event.type == pygame.QUIT:
            is_running = False
        # press key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -3
            if event.key == pygame.K_RIGHT:
                player_x_change = 3
            if event.key == pygame.K_SPACE and (not bullet_visible):
                bullet_sound = mixer.Sound('python1/Day10/shot.mp3')
                bullet_sound.play()
                bullet_x = player_x
                shoot_bullet(bullet_x, bullet_y)
        # release key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    # modify location
    player_x += player_x_change
        
    # keeping rocket inside screen
    if player_x <= 0:
        player_x =0
    if player_x >=736:
        player_x = 736
        
    # modify location
    for enem in range(number_of_enemy):
        if enemy_y[enem] > 450:
            for k in range(number_of_enemy):
                enemy_y[k] = 800
            final_text()
            break
        enemy_x[enem] += enemy_x_change[enem]
        
    # keeping rocket inside screen
        if enemy_x[enem] <= 0:
            enemy_x[enem] = 64
            enemy_x_change[enem] = 2
            enemy_y[enem] += enemy_y_change[enem]
        if enemy_x[enem] >=736:
            enemy_x[enem] = 735
            enemy_x_change[enem] = -2
            enemy_y[enem] += enemy_y_change[enem]
        
        # collition
        collition = there_is_collition(bullet_x,bullet_y, enemy_x[enem], enemy_y[enem])
        if collition:
            collition_sound = mixer.Sound('python1/Day10/punch.mp3')
            collition_sound.play()
            bullet_y = 536
            bullet_visible = False
            score += 1
            enemy_x[enem] = random.randint(0,736)
            enemy_y[enem] = random.randint(50,200)
            
        enemy(enemy_x[enem], enemy_y[enem], enem)

    if bullet_y < -64:
        bullet_y = 536
        bullet_visible = False
    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

        
    player(player_x, player_y)
    show_score(text_x,text_y)
    pygame.display.update()